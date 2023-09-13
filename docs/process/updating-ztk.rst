Updating the ZTK itself
=======================

To get new version pins into ZTK run the following steps:

* ``tox -e checkversions | grep "="``

  This command lists the packages where newer versions are available. (The grep
  is needed to omit the other rubbish rendered by the command call.)
* Update ``ztk-versions.cfg`` with these new versions and run ``tox`` to run their
  tests.
* Run the checkversion call from above again to make sure all possible versions
  are updated.
* If the test runs are successful: create a pull request on GitHub.
