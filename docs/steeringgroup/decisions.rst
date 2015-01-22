Decisions
=========

This is a temporary place to note decisions. The idea is to later
integrate them into the Zope Toolkit documentation, but we need a
quick way to note decisions first.

* ZMI related code shall not be part of the Zope Toolkit, and we
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

* if you think a new "extra" dependency is needed in a Zope Toolkit
  package, and you're not just moving stuff between packages but
  actually developing new code, bring it up on zope-dev so we can at
  least consider alternatives. Perhaps a better home can be found for
  this code.

* We can consider removing extra dependencies for particular Zope
  Toolkit packages in order to make the dependency graph easier to
  reason about. We will do this on a case by case basis though.
  
* In namespace package's ``__init__.py`` we have been using the following
  boilerplate code::

    try:
        import pkg_resources
        pkg_resources.declare_namespace(__name__)
    except ImportError:
        import pkgutil
        __path__ = pkgutil.extend_path(__path__, __name__)

  Since ``setuptools`` is a dependency of our packages anyway, we 
  can instead do the following::

      __import__('pkg_resources').declare_namespace(__name__)

  Feel free to use that and also feel free to simplify existing
  ``__init__.py`` modules. Just make sure ``setuptools`` is a declared
  dependency of the package.

* Moving code around as part of dependency refactoring is worth a
  feature release (x.y as opposed to x.y.z version number) for the
  affected packages. Changing an import to make use of a new package
  that came out of such refactoring is also worth a feature release.

* If a package A starts to rely on new features in dependency B,
  that is worth a feature release of package A.

* The version requirements in setup.py should specify only API
  compatibility.  They should not specify a dependency on bug fixes;
  that's the domain of the KGS.

  Therefore in a ``setup.py`` you are allowed to write this in ``setup.py``::

    bar >= x.y

  I.e. relying on a newer feature release of package ``bar``.

  but not this::

    bar >= x.y.z

  I.e. you're not allowed to rely on a newer *bugfix* release of
  package ``bar``.

  Elaboration: Imagine package ``foo`` that depends on package
  ``bar``. If you make changes in ``foo`` so that it starts to rely on
  changes in ``bar`` that are only introduced in a feature release of
  ``bar`` (``bar`` version ``x.y`` or ``bar`` version ``x``), you
  should update the ``setup.py`` of ``foo`` to state this dependency
  with a requirement like this::

    bar >= x.y

  This is only relevant to *feature* releases. If there is a bugfix
  release of ``bar`` you should not write a dependency like ``bar >=
  x.y.z``.

  This is a compromise in the interests of both flexibility and giving
  hints to people who use our packages. We'll see how it goes.

* Some Zope Toolkit packages are quite reusable without having to buy
  into the rest of the Zope Toolkit. Others aren't reusable at all
  without pulling in a huge chunk of the Zope Toolkit; they depend on
  many assumptions.

  We should communicate this clearly to potential users. As a first
  step, we will make sure these notifications are available on the
  PyPI pages. We will do this by adding a message about reusability to
  the long_description (which gets displayed on PyPI). Typically this
  is done by modifying the package's README.txt or
  ``src/zope/../README.txt`` doctest.

  The following text should be used for reusable packages::

    *This package is intended to be independently reusable in any Python
    project. It is maintained by the* `Zope Toolkit project
    <http://docs.zope.org/zopetoolkit/>`_.

  The following text should be used for packages that are *not*
  easily reusable::

    *This package is at present not reusable without depending on a
    large chunk of the Zope Toolkit and its assumptions. It is
    maintained by the* `Zope Toolkit project
    <http://docs.zope.org/zopetoolkit/>`_.

  At the time of writing, most of our packages will be marked as *not*
  reusable. Only packages at the roots of our dependency tree that
  have a clear purpose and some documentation (such as
  ``zope.interface`` and ``zope.component``) should be marked as
  reusable. We will slowly start to build up from there.

* When code moves to a new location to import it from (in the same or
  another package), use a ``from foo import bar`` statement, with a
  ``#BBB`` comment to indicate the import is only there to support
  backwards compatibility.

  In the CHANGES.txt of a package, state that an import location got
  deprecated and where the new location is (making this a feature
  release, not a bugfix release).

  Reasons:

  * it avoid a dependency on zope.deprecation, which is quite involved
    in its implementation, using proxies.

  * A ``from .. import ..`` is immediately comprehensible to any
    Python programmer as well as tools.
  
  * Deprecation warnings make it hard to write a library that supports
    multiple versions of another library; a change in an indirect
    dependency can create deprecation warnings that the original
    developer does not care about.

  * We are in the process of developing a testrunner extension that
    will report on indirect imports, and a ZODB upgrade procedure.

* The open issues will be moved to the launchpad blueprints and
  launchpad answers. The blueprint specifications will be stored in
  the ZTK documentation and linked to (each blueprint will be a
  separate document).

* As a general direction we'd like to separate out the XML-RPC related
  code and FTP-related code into seperate packages that aren't
  depended on by the rest of the toolkit. This makes it possible for
  developers to use the toolkit without worrying about XML-RPC or FTP.

* To make it easy for developers to identify which packages are in the
  ZTK, as they are sometimes working in isolation, a package that is
  maintained by the Zope Toolkit project should have the following
  text in its ``setup.py`` file just under the copyright header::

    ##############################################################################
    # This package is developed by the Zope Toolkit project, documented here:
    # http://docs.zope.org/zopetoolkit
    # When developing and releasing this package, please follow the documented
    # Zope Toolkit policies as described by this documentation.
    ##############################################################################

  When a package is *removed* from the ZTK this header should be removed
  from its ``setup.py`` as well.

* There was a discussion about whether the version in ``setup.py``
  should be set to ``0`` instead of the next expected version. There
  was a discussion and the majority of the steering group was against
  this change - the ZTK release policy remains the same for the ZTK.

  The mailing list threads discusses various pros and cons::

    https://mail.zope.org/pipermail/zope-dev/2009-September/037725.html

    https://mail.zope.org/pipermail/zope-dev/2009-September/037735.html

* We want to encourage narrative documentation for packages (doctested
  or not). Even though we do not require that this documentation is
  executable (doctested), we do prefer a project setup so that it easy
  to support executable documentation as well, in cooperation with
  tools like manuel. The bobo documentation is an example of such a
  setup. We should document this better.
