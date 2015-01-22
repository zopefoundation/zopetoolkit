Package Usage
=============

These tables show which packages are used by which frameworks. Plone is
included for reference only.

The following abbreviations are used in the table:

B = BlueBream
G = Grok
2 = Zope
P = Plone

x = is used
_ = is not used

We do not differentiate the type of dependency (direct or transitive). At this
point we are only interested if a package is required by a framework in some
way or not.

In a ``zopepy`` interpreter one can get all active distributions with::

  import pprint, pkg_resources
  pprint.pprint(sorted([p.project_name for p in pkg_resources.working_set.by_key.values()]))

ZTK
---

= = = = =============================
B G 2 P Package name
= = = = =============================
x x x x zope.annotation
x _ _ _ zope.applicationcontrol
x x _ x zope.authentication
x x x x zope.broken
x x x x zope.browser
x x x x zope.browsermenu
x x x x zope.browserpage
x x x x zope.browserresource
x x _ x zope.cachedescriptors
_ x _ _ zope.catalog
x x x x zope.component
x x _ x zope.componentvocabulary
x x x x zope.configuration
x x x x zope.container
_ x x x zope.contentprovider
x x x x zope.contenttype
x x _ x zope.copy
x x _ x zope.copypastemove
x x _ x zope.datetime
x x x x zope.deferredimport
x x _ x zope.deprecation
_ _ _ _ zope.documenttemplate
x x x x zope.dottedname
x x _ x zope.dublincore
x x _ x zope.error
x x x x zope.event
x x x x zope.exceptions
x x x x zope.filerepresentation
x x _ x zope.formlib
x x _ x zope.hookable
x x x x zope.i18n
x x x x zope.i18nmessageid
_ x _ _ zope.index
x x x x zope.interface
_ x _ _ zope.intid
_ x _ _ zope.keyreference
x x x x zope.lifecycleevent
x x x x zope.location
x x _ x zope.login
_ _ _ _ zope.mimetype
x x _ x zope.minmax
x x x x zope.pagetemplate
x x _ x zope.password
x x _ x zope.pluggableauth
x x _ _ zope.principalannotation
x x _ x zope.principalregistry
x x x x zope.processlifetime
x x x x zope.proxy
x x x x zope.ptresource
x x x x zope.publisher
_ _ _ x zope.ramcache
x x x x zope.schema
x x x x zope.security
x x _ x zope.securitypolicy
_ _ x x zope.sendmail
_ _ x x zope.sequencesort
_ _ _ _ zope.server
x x _ x zope.session
x x x x zope.site
x x x x zope.size
x x x x zope.structuredtext
x x x x zope.tal
x x x x zope.tales
x x x x zope.testing
x x x x zope.traversing
_ x x x zope.viewlet
= = = = =============================
