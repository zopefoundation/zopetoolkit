# Generate package list information for trunk and tags of ZTK.

try:
    from ConfigParser import RawConfigParser, Error
except ImportError:
    from configparser import RawConfigParser, Error
import io
import os
import socket
import subprocess
import sys
try:
    from urllib2 import urlopen, HTTPError
except ImportError:
    from urllib.request import urlopen
try:
    from urllib2 import HTTPError
except ImportError:
    from urllib.error import HTTPError
import xml.etree.ElementTree

from pkg_resources import parse_version

socket.setdefaulttimeout(15)


TABLE_HEADER = """\
.. list-table::
    :class: packagelist
    :widths: 25 10 40 25
    :header-rows: 1

    * - Name
      - Version
      - Description
      - Links\
"""

PACKAGE_LINE_BASE = """
    * - `%(name)s <%(homepage)s>`_
      - %(version)s
      - %(description)s\
"""

DEPENDENCY_PACKAGE_LINE = PACKAGE_LINE_BASE + """
      - \
"""

PACKAGE_LINE = PACKAGE_LINE_BASE + """
      - `Bugs <http://github.com/zopefoundation/%(name)s/issues>`__ |
        `Git <https://github.com/zopefoundation/%(name)s>`__ \
"""

GENERATED_WARNING = """\
.. This file is generated. Please do not edit manually or check in.
"""

DOAP_NS = 'http://usefulinc.com/ns/doap#'
TAGS_DIR = os.path.join(os.pardir, 'tags')

RELEASE_OVERVIEW = """
This document covers major changes in this release that can lead to
backward-incompatibilities and explains what to look out for when updating.
"""

RELEASE_PACKAGES = """

List of packages
----------------

.. toctree::
   :maxdepth: 1

   packages-%(release)s
"""

RELEASES_OVERVIEW = """
Releases
========

This area collects release-specific information about the toolkit including a
list of backward-incompatible changes, new techniques developed, and libraries
included.

.. toctree::
   :maxdepth: 1

"""


def package_list(packages, config, _lineout, line=PACKAGE_LINE):
    lines = [TABLE_HEADER]
    for package in sorted(packages):
        version = config.get('versions', package)
        try:
            doap_xml = urlopen(
                'http://pypi.python.org/pypi?:action=doap&name=%s&version=%s' %
                (package, version)).read().decode('utf-8')
        except HTTPError:
            return
        if not doap_xml:
            # someone removed a released package from PyPi - ARGHHH!
            return
        doap_xml = io.StringIO(doap_xml.replace('\f', ''))
        doap = xml.etree.ElementTree.ElementTree()
        doap.parse(doap_xml)
        description = doap.find('.//{%s}shortdesc' % DOAP_NS).text
        homepage = 'http://pypi.python.org/pypi/%s/%s' % (package, version)
        lines.append(line % dict(name=package,
                                 homepage=homepage,
                                 description=description,
                                 version=version,
                                ))
    lines.append('')
    for line in lines:
        _lineout(line)


def packages(config, key):
    result = config.get('ztk', key).split('\n')
    result = filter(None, map(str.strip, result))
    return result


def find_releases():
    """Return a list of ZTK releases.
    """
    yield ('trunk', 'master')

    lines = subprocess.check_output(['git', 'tag', '-l']).strip().splitlines()
    lines = [x.decode('ascii') for x in lines]
    for line in sorted(lines, key=parse_version, reverse=True):
        tag = line.strip()
        if 'dev' not in line:
            yield (tag, tag)

def only_if_missing(releases):
    for release in releases:
        version, _ = release
        if not os.path.exists(
                os.path.join('docs/releases', 'overview-%s.rst' % version)):
            yield release

def main(releases):

    def _lineout(msg, *args):
        output.write('%s\n' % (msg % args))

    if not releases:
        releases =  list(only_if_missing(find_releases()))

    for release, tag in releases:
        print("Writing package list for %s" % release)
        config = RawConfigParser()
        config.optionxform = str
        cfg = subprocess.check_output(['git', 'show', '%s:ztk.cfg' % tag])
        try:
            config.read_string(cfg.decode('ascii'))
        except Error as e:
            print("Unable to parse config: %s" % str(e))
            continue

        versions = RawConfigParser()
        versions.optionxform = str
        cfg = subprocess.check_output(
                                ['git', 'show', '%s:ztk-versions.cfg' % tag])
        try:
            versions.read_string(cfg.decode('ascii'))
        except Error as e:
            print("Unable to parse versions: %s" % str(e))
            continue

        with open(os.path.join('docs', 'releases',
                               'packages-%s.rst' % release), 'w') as output:

            _lineout(GENERATED_WARNING)

            _lineout('')
            _lineout('.. _packages-%s:' % release)
            _lineout('')
            heading = 'Zope Toolkit %s packages' % release
            _lineout(heading)
            _lineout('=' * len(heading))
            _lineout('')
            _lineout('See :ref:`overview-%s`.' % release)
            _lineout('')
            included = list(packages(config, 'included'))
            package_list(included, versions, _lineout)

            deprecating = list(packages(config, 'deprecating'))
            if deprecating:
                _lineout('Deprecating')
                _lineout('-----------')
                package_list(deprecating, versions, _lineout)

            _lineout('Dependencies')
            _lineout('------------')
            all = versions.options('versions')
            dependencies = set(all) - (set(included) | set(deprecating))
            package_list(dependencies, versions, _lineout,
                         DEPENDENCY_PACKAGE_LINE)


        with open(os.path.join('docs', 'releases',
                               'overview-%s.rst' % release), 'w') as output:
            _lineout(GENERATED_WARNING)
            _lineout('')
            _lineout('.. _overview-%s:' % release)
            _lineout('')
            title = "Zope Toolkit %s" % release
            _lineout(title)
            _lineout("=" * len(title))
            _lineout(RELEASE_OVERVIEW)
            index = subprocess.check_output(
                                    ['git', 'show', '%s:index.rst' % tag])
            _lineout(index.decode('utf-8'))
            _lineout(RELEASE_PACKAGES % {'release': release})

    print("Writing overview")

    with open(os.path.join('docs', 'releases', 'index.rst'), 'w') as output:
        TRUNK = 'overview-trunk.rst'
        _lineout(GENERATED_WARNING)
        _lineout(RELEASES_OVERVIEW)
        overviews = list(
                      reversed(
                        sorted([x for x in os.listdir('docs/releases')
                                    if x.startswith('overview')])))
        has_trunk = TRUNK in overviews
        if has_trunk:
            overviews.remove(TRUNK)
            overviews.insert(0, TRUNK)
        for overview in overviews:
            _lineout('   %s' % overview)


if __name__ == '__main__':
    args = []
    for arg in sys.argv[1:]:
        if ':' in arg:
            args.append(tuple(arg.split(':', 1)))
        else:
            args.append((arg, arg))
    main(args)
