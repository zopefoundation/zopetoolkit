Open Issues
===========

These are issues that are currently under discussion and on which the
steering group will want to make a decision soon.

* Do we want to deprecate the deprecation system? See
  http://mail.zope.org/pipermail/zope-dev/2009-March/035130.html

* Python 3 may collide with __annotations__. In the last years Python
  clarified that the language claims __*__ attributes so we need to figure out
  how to deal with the occurances where we use those attributes (__name__,
  __parent__)
  http://mail.zope.org/pipermail/zope-dev/2009-March/035237.html

* Produce a list of `the toolkit packages`. See
  http://mail.zope.org/pipermail/zope-dev/2009-March/035078.html.

* Document usage of compattest. `compattest` is being mentioned for
  test runs and should be documented as an (optional) part of the toolkit
  development.

* Support using ``setup.py test``? See
  http://mail.zope.org/pipermail/zope-dev/2009-March/035240.html

* We should investigate the possible role of WebOb in the Zope
  Toolkit. See http://mail.zope.org/pipermail/zope-dev/2009-March/034870.html

* When can we give up Python 2.4 compatibility for new releases of
  packages? The following decision didn't please everybody:

  * New feature releases of packages in the Zope Toolkit should be
    compatible with Python 2.5 (and 2.6, preferably). Python 2.4
    compatibility is not required.
 
    The following low-level packages are exceptions that do still need
    Python 2.4 compatibility:

    * zope.interface, zope.schema, zope.component, zope.event,
      zope.i18nmessageid

* publisher and traversal simplification: Shane Hathaway's WSGI
  pipeline work, Jim's new bobo should be points to explore.

* reusable components that include a UI. Might be separated into two
  components (API and UI), or even three (API, web service and
  UI). Example use cases are user management and tagging. Explore
  Pinax for more examples. The irony and great potential of the ZTK
  right now is that we *have* a component story that works pretty well
  so we *should* be able to do great flexible UI components, but we
  don't have a good story for this at all.

* dependency refactoring: this is an ongoing process to try to flatten
  the dependency structure between packages and allow greater reusability
  of our code, and reduce the amount of code that is needed in a minimal
  setup (less to understand, and less startup time).

* startup time: reduce the startup time of ZTK applications so that 
  the paster auto-restart becomes more tolerable. 

* We need a process to implement new functionality/features within the ZTK.
  There seems to be some tendency to implement new functionality in each
  framework/project without a backchannel to share results on a common basis.
