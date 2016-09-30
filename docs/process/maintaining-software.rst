Maintaining software
====================

:Author: Philipp von Weitershausen <philipp@weitershausen.de>
:Status: Draft


.. contents::


Introduction
------------

This guide outlines rules, recommendations and best practices for
authors of software (mainly Python packages) that lives in the Zope
software repository.  It does not impose any new rules on existing
software.  It is mostly a written-down collection of rules,
recommendations and best practices that have been maintained within
the Zope community for some time now, some more than others.

Therefore, the main purpose of this document is to document those
existing practices for people who've joined the Zope project recently,
and to serve as a canonical source for guidance when in doubt.


Repository layout
-----------------

Here's an example of naming conventions used in the Zope Github
organization at ``github.com/zopefoundation``::

  zope.component/
  zope.component/branches/
  zope.component/branches/3.4
  zope.component/branches/philikon-100x-faster
  ...
  zope.component/tags/
  zope.component/tags/3.4.0
  zope.component/tags/3.4.0b1
  zope.component/tags/3.4.1
  ...
  zope.component/master/
  ...

To summarize:

* The Github project name is the project's name. This is also
  the name of the Python distribution.  If it contains just
  one package, the dotted name of the package should be used for the
  project name, e.g. ``zope.component``, ``z3c.form``.  The same is
  true for Zope 2 "products", e.g. ``Products.Five`` (note that not
  all products adhere to this for legacy reasons, new projects should
  use this convention, however).

  It is recommended to put software in a namespace package to avoid
  name clashes.  Valid choices for namespace package names are:

  * ``zope``, although this one is used by the Zope platform itself
    and should only be used for new projects after approval from the
    community.

  * ``z3c`` (meaning "Zope 3 Community")

  Sometimes the project doesn't hold just one package but a number of
  packages or not even software at all.  In this case pick a
  meaningful name that's unlikely to interfere with other names.

* Release branches and release tags should be simple dotted numbers
  stating the version that the branch or tag is for.  Use ``3.4``, not
  ``3.4.x`` or something else, for the release branch that's
  responsible for ``3.4.0``, ``3.4.1``, etc.

* Branches for doing temporary work (such as refactorings) should
  begin with the login name of the primary author and then feature a
  short and descriptive name of what they're about.  For example,
  ``philikon-100x-faster`` indicates that Philipp von Weitershausen is
  working in making ``zope.component`` 100 times faster.  You wish...

  Temporary work branches should be short-lived and *removed* once
  they're merged.  Release branches and tags should never be removed.
  Release tags shouldn't be committed to once the release has been
  announced and distributed.


License
-------

Unless allowed otherwise, all software committed to the Zope
organization is subject to the `Zope Public License (ZPL)`_.  The
documentation of the software should state so.  In addition, each
source code file should contain the following license header at the
top::

  ##############################################################################
  #
  # Copyright (c) 2016 Zope Foundation and Contributors.
  # All Rights Reserved.
  #
  # This software is subject to the provisions of the Zope Public License,
  # Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
  # THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
  # WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  # WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
  # FOR A PARTICULAR PURPOSE.
  #
  ##############################################################################

The year and the current version of the ZPL are to be adjusted, of
course.

.. _Zope Public License (ZPL): http://www.zope.org/Resources/ZPL


Coding style
------------

When starting new packages, one should adhere to the coding style
suggested by `PEP 8`_.  When modifying or enhancing existing software,
the package's existing coding style should be used.

.. _PEP 8: http://www.python.org/dev/peps/pep-0008/


Automated tests
---------------

All software should be accompanied by automated tests.  Packages that
provide integrated components for the web should preferrably be
accompanied by both unit tests and integration/functional tests.  The
definition of test cases should be done in ``tests`` packages or
modules.

Before checking modifications into the trunk or a release branch, all
existing tests for the package must pass.  Furthermore, when adding a
feature, modifying the behaviour of a component or fixing a bug, a
test exercising the change must be supplied as well.  There would
otherwise be no reproducible way of knowing whether the new code
actually worked.  In terms of automated tests, think "Untested code is
broken code."

Tests should be written in a fairly literate way with documentation of
the test itself.  That is to ensure that the intent of each test is
clear and obvious to any other developer.  One should use
``unittest.TestCase`` as a test harness.


Backward-compatibility
----------------------

As a rule of thumb, backwards-incompatible changes to stable, released
code should be avoided.  Examples of backwards-incompatible changes
are

* renaming packages, modules, classes, functions, etc. without
  ensuring the old import paths still work,

* changing a public interface, which also includes *adding* attributes
  or methods (imagine people implemented this interface in their own
  code, now all of a sudden their implementations don't comply with
  the interface anymore)

If you'd like to replace a certain component or package with another,
better one, don't remove the original component or package, not even
after a deprecation period.  Instead, consider simply abandoning the
original component or package.  You should clearly document that, of
course, possibly even by raising DeprecationWarnings.  Then you
provide the replacement under a separate name.

For example, consider you would like to radically improve a package
``mycorp.foo``.  Instead of changing it in an incompatible way, you
should just stop supporting it and create ``mycorp.newfoo`` (or
whatever you'd like to name it).

Consistency weighs higher than cleanliness.


Package documentation and metadata
----------------------------------

It is recommended that all packages in the Zope repository are
accompanied by at least the following minimum set of documentation and
metadata (file names are relative to the package's distribution, in
terms of a checkout they're relative to ``master`` or a release branch
or tag):

``README.rst``
    This file should give an overview over what the package or project
    is about.  It is acceptable for this to be just a few paragraphs
    or a full-fledged manual for the piece of software.

    If the package has an associated mailinglist and a bugtracker, it
    is a good idea to mention it here.

    This file should contain valid reStructuredText_.

    Here's an example for a short file containing only a few
    paragraphs, but referring to a separate documentation site::

      Martian provides infrastructure for declarative configuration of
      Python code. Martian is especially useful for the construction of
      frameworks that need to provide a flexible plugin infrastructure.

      Martian provides a framework that allows configuration to be expressed
      in declarative Python code. These declarations can often be deduced
      from the structure of the code itself. The idea is to make these
      declarations so minimal and easy to read that even extensive
      configuration does not overly burden the programmers working with the
      code. Configuration actions are executed during a separate phase
      ("grok time"), not at import time, which makes it easier to reason
      about and easier to test.

      For more information about using Martian, see:

        martian.readthedocs.io

``CHANGES.rst``
    This file contains the changelog.  The changelog should keep track
    of every new feature and every bugfix of all releases.  When a
    particular release has lots of changes, it may group them into
    "Features" and "Bugfixes".  The release date should be given for
    each release in the ISO 8601 dash notation (YYYY-MM-DD).  For
    example::

      1.1 (unreleased)
      ----------------

      * ...

      1.0 (2007-01-24)
      ----------------

      * Fixed a memory leak.

      * Improved documentation a lot.

      0.9 (2006-12-05)
      ----------------

      * Initial preview release.

    This file should contain valid reStructuredText_.

``setup.py``
    Most Python software is distributed using distutils and
    setuptools.  By convention, the script to do the packaging should
    be called ``setup.py``.  The following example outlines the
    *minimum* package metadata that it should contain::

      from setuptools import setup, find_packages

      long_description = (open('README.txt').read() +
                          '\n\n' +
                          open('CHANGES.txt').read())

      setup(
          name='z3c.awesomelib',
          version='2.0.0.dev',
          url='http://pypi.python.org/pypi/z3c.awesomelib',
          author='Philipp von Weitershausen',
          author_email='philipp@weitershausen.de',
          license='ZPL 2.1',
          classifiers=['Environment :: Web Environment',
                       'Intended Audience :: Developers',
                       'License :: OSI Approved :: Zope Public License',
                       'Programming Language :: Python',
                       'Operating System :: OS Independent',
                       'Topic :: Internet :: WWW/HTTP',
                       ],
          description="An awesome website implementation.",
          long_description=long_description,

          packages=find_packages('src'),
          package_dir={'': 'src'},
          namespace_packages=['z3c'],
          include_package_data=True,
          install_requires=['setuptools', 'zope.interface, 'zope.component']
          zip_safe=False,
          )

    To elaborate on this example:

    * The blank line separates mostly informational metadata intended
      for users from packaging metadata intended for setuptools.

    * Many packages don't have their own "homepage". It
      is often more convenient to use the `Python Package Index
      (PyPI)`_ as a homepage for the package (via the ``url``
      parameter) since PyPI renders ``long_description`` for the
      package's main page and provides downloads.

    * The list of `Trove classifiers`_ (``classifiers`` parameter)
      should be adjusted according to the specific package, of course.
      Much of the software in the Zope repository is intended to be
      used with Zope 2 or the Zope Toolkit (sometimes for both), we
      aim to make more and more software available for independent use
      (well-known examples are ``zope.interface`` or the ``ZODB``).

    * ``description`` should be a one-sentence description of the
      package while ``long_description`` is best taken from the
      ``README.rst`` file as demonstrated.  You may also include the
      changelog in ``long_description`` by concatenating ``README.rst
      and ``CHANGES.rst``.

.. _reStructuredText: http://docutils.sourceforge.net/rst.html
.. _Python Package Index (PyPI): http://pypi.python.org/pypi
.. _Trove classifiers: http://pypi.python.org/pypi?%3Aaction=list_classifiers
