from docutils import nodes
from sphinx.util.compat import Directive
import json

import urllib
import socket
import threading


def setup(app):
    app.add_config_value('buildbot_check', True, 'html')
    app.add_node(BuildbotColor,
                 html=(visit_buildbot_node, depart_buildbot_node))
    app.connect('doctree-resolved', process_buildbot_nodes)
    app.add_directive('buildbotresult', BuildbotDirective)


class BuildbotDirective(Directive):

    has_content = True
    required_arguments = 1
    optional_arguments = 1
    final_argument_whitespace = True

    def run(self):
        buildbot_url = self.arguments[0]
        text = self.arguments[1]
        targetnode = BuildbotColor('', '')
        targetnode.text = text
        targetnode.buildbot_url = buildbot_url

        return [targetnode]


def process_buildbot_nodes(app, doctree, fromdocname):
    if not app.config.buildbot_check:
        return
    socket_timeout = socket.getdefaulttimeout() or 5
    try:
        socket.setdefaulttimeout(min(socket_timeout, 5))
        by_url = {}
        for node in doctree.traverse(BuildbotColor):
            url = parse_builder_url(node.buildbot_url)
            by_url.setdefault(url, []).append(node)
        jobs = []
        for url, nodes in by_url.items():
            if not nodes:
                continue
            thread = threading.Thread(target=update_buildbot_nodes,
                                      args=(url, nodes),
                                      name='%s' % (url,))
            thread.start()
            jobs.append(thread)
        for thread in jobs:
            thread.join()
    finally:
        socket.setdefaulttimeout(socket_timeout)


def parse_builder_url(url):
    """Parse a builder URL into buildbot URL and builder name."""
    # make sure trailing slashes don't cause failures
    url = url.rstrip('/').split('/')
    cut_index = url.index('builders')
    json_url = '/'.join(url[:cut_index] + ['json'] + url[cut_index:])
    return json_url


def update_buildbot_nodes(url, nodes):
    """Get build status of a number of builders and update document nodes.

    ``nodes_and_builders`` is a list of tuples (node, builder_name).
    """
    result = get_buildbot_result(url)
    for node in nodes:
        if isinstance(result, Exception):
            node.css_class = 'tests_could_not_determine'
            node.title = '%s: %s' % (result.__class__.__name__, result)
        elif result:
            node.css_class = 'tests_passed'
        else:
            node.css_class = 'tests_not_passed'


def get_buildbot_result(json_url):
    """Return build status of a number of builders.

    ``builders`` is a list of builder names.

    Returns a dictionary mapping builder names to True/False or exception
    objects, in case of errors.
    """
    try:
        data = json.load(urllib.urlopen(json_url + '/builds/-1'))
        print(data['text'])
        return u'successful' in data['text']
    except Exception as e:
        return e

class BuildbotColor(nodes.Inline, nodes.TextElement):
    pass


def visit_buildbot_node(self, node):
    kwargs = {'href' : node.buildbot_url}
    css_class = getattr(node, 'css_class', '')
    if css_class:
        kwargs['class'] = css_class
    title = getattr(node, 'title', '')
    if title:
        kwargs['title'] = title
    self.body.append(self.starttag(node, 'a', **kwargs))
    self.body.append(node.text)


def depart_buildbot_node(self, node):
    self.body.append('</a>')

