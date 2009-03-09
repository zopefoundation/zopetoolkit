Decisions of the Zope Framework Steering Group
==============================================

* ZMI related code shall not be part of the Zope Framework, and we
  shall strive to remove it.

* If zope.deferredimport is used in a package merely to avoid the use
  of ``from`` imports, then instead we will use ``from`` imports to
  get rid of this dependency.

* Files used to support the old ZPKG system such as ``DEPENDENCIES.cfg``
  can be safely removed from packages.

* So-called "ZCML-slugs" which were intended to be symlinked into a
  special slugs directory in a Zope installation are not in use
  anymore.  They should be removed. Typically they look like
  ``zope.foo-configure.zcml``.

* we are going to work at getting rid of the zope.app.testing extra by
  distributing its facilities into individual zope.*
  packages. Hopefully we can get a clear consensus on this one from
  the people who object to the general policy.

* if you think a new "extra" dependency is needed in a Zope Framework
  package, and you're not just moving stuff between packages but
  actually developing new code, bring it up on zope-dev so we can at
  least consider alternatives. Perhaps a better home can be found for
  this code.

* on a case-by-case basis we can consider removing extra dependencies
  for particular Zope Framework packages, just like what we're doing
  right now for zope.component. We'll discuss that whenever
  needed.
