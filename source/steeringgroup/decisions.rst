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
