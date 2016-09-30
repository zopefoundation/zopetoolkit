Releasing software
------------------

When releasing software, the following steps should be taken:

1. Make sure all automated tests of the package pass and there are no
   release-critical bugs in its bug tracker.

2. Fill in the release date in ``CHANGES.rst``. Make sure the
   changelog is complete. Update the version number in ``setup.py`` and
   remove the ``dev`` marker.

   Also consider the version number for the new release. If the API
   has been added to, or the behavior has otherwise changed in a way
   that goes beyond a bugfix, please update the version number for the
   next release and make it a feature release (x.y) instead of a
   bugfix release (x.y.z).

3. Make sure the package metadata in ``setup.py`` is up-to-date.  You
   can verify the information by re-generating the egg info::

     python setup.py egg_info

   and inspecting ``src/EGGNAME.egg-info/PKG-INFO``.  You should also
   make sure the that the long description renders as valid
   reStructuredText.  You can do this by using the ``rst2html.py``
   utility from docutils_::

     python setup.py --long-description | rst2html.py > test.html

   If this will produce warnings or errors, PyPI will be unable to
   render the long description nicely.  It will treat it as plain text
   instead.

4. Create a release tag.

5. Get a separate checkout of the release tag for creating the
   distribution tarball and eggs.  It is important that you don't do
   this on the master or release branch to avoid

   - forgetting to tag the release at all.

   - forgetting to clean up the ``build`` directory that distutils and
     setuptools create. Failure to do so may result in old artefacts
     in eggs.

   - forgetting to check in files that are needed by ``setup.py`` or
     as package data.  Setuptools will only include them in the
     distribution if they are specifed by the ``MANIFEST.in``.

   In the checkout of the tag create a distribution and upload it to PyPI
   using the following command::

     python setup.py register sdist upload

6. Back on the master or the release branch, increase the version
   number in ``setup.py`` to the *next* release and add back the
   ``dev`` marker.  The convention is that the master or release branch
   always points to the upcoming release, *not* the one that has been
   released already.  So if you've just released version 3.4.1, you
   should change ``setup.py`` to read::

     setup(
         name='...',
         version='3.4.2.dev',
         ...
         )

   In ``CHANGES.rst`` add a *new* section for the upcoming release.
   The release date for that should say "unreleased" so that
   committers recording their changes won't accidentally put their
   entry in the section for an already released version.  For
   example::

     3.4.2 (unreleased)
     ------------------

     * ...

     3.4.1 (2007-01-24)
     ------------------

     * Fixed bug in the foo adapter.

     * Added a bar utility for optimized kaboodling.

     3.4.0 (2006-09-13)
     ------------------

     Initial release as separate egg.

**Important:** Once released to PyPI or any other public download
location, a release may *never* be removed, even if it has proven
to be a faulty release ("brown bag release").  In such a case it
should simply be superseded immediately by a new, improved release.

.. _docutils: http://docutils.sourceforge.net/
