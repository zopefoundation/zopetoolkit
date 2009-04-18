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

.. note:: 
   We may want to move over the management of such issues to
   launchpad? Not?

