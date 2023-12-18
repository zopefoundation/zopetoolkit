Updating the ZTK itself
=======================

Updating versions of dependencies
---------------------------------

To get new version pins into ZTK run the following steps:

* ``tox -e checkversions | grep "="``

  This command lists the packages where newer versions are available. (The grep
  is needed to omit the other rubbish rendered by the command call.)
* Update ``ztk-versions.cfg`` with these new versions and run ``tox`` to run their
  tests.
* Run the checkversion call from above again to make sure all possible versions
  are updated.
* If the test runs are successful: create a pull request on GitHub.

Creating a release
------------------

* Make sure all tests are running successfully.
* Decide on a version number for the new release, taking https://semver.org/
  into account. (Please note: dropping support for a Python version is
  considered a major change as it enforces changes for users of ZTK who are
  using the no longer supported Python version.)
* Create a change log page in ``doc/releases`` with the name of your release
  number and describe the most important changes in the new release.
* Add the name of the file to ``doc/releases/index.rst``.
* Check the documentation builds using ``tox -e docs`` and proof-read your
  changes.
* Commit your newly added file via ``git``.
* Create a git tag using ``git tag`` and your version number.
* Push your changes, make sure also the tag is pushed.
* Switch to the branch ``gh-pages``.
* Run ``build_indexes.sh``, add and commit the changes.
* Push the changes to GitHub, after some seconds the changes should appear at
  https://zopefoundation.github.io/zopetoolkit/.
