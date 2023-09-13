====================
Automated test suite
====================

The ZTK's automated test suite builds on the individual packages' unit and
functional tests and creates a combined test runner that runs each packages'
test suite in isolation but ensures that the dependencies are satisfied using
the ZTK versions under test.

The combined test runner is created using `z3c.recipe.compattest
<https://github.com/zopefoundation/z3c.recipe.compattest>`_ -- check its
documentation for details.

If you take a ZTK checkout, you can run the tests yourself like this::

    $ git clone git@github.com:zopefoundation/zopetoolkit.git
    $ tox -pauto

If you work on a ZTK package and want to ensure that your changes are
compatible with all other ZTK libraries, you can use a checkout of the
individual package inside the zopetoolkit checkout::

    $ bin/develop co zope.component
    $ bin/develop rb
    $ bin/test-ztk

The develop commands get a git checkout of the specified package and
puts it into the develop/ folder, so you make your changes there.
