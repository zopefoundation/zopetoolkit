The Zope Toolkit
================

.. image:: https://travis-ci.com/zopefoundation/zopetoolkit.svg?branch=master
        :target: https://travis-ci.com/zopefoundation/zopetoolkit

.. image:: https://readthedocs.org/projects/zopetoolkit/badge/?version=latest
        :target: http://zopetoolkit.readthedocs.io/en/latest/
        :alt: Documentation Status

The Zope Toolkit is a set of libraries maintained by the Zope project for
building web applications, web frameworks and application servers.

It supports Python 3.7 up to 3.1 as well as PyPy 3.

This directory contains the definition of the Zope Toolkit in the file
``ztk.cfg``. It specifies the list of packages included in the ZTK and
packages which are under review for inclusion.

Also, specific versions have been tested together (including their
dependencies) and can directly be used with a buildout by specifying the
``ztk-versions.cfg`` file via the ``extends`` mechanism.

To test the ZTK, run ``bin/test-ztk`` or ``tox`` for all supported Python
versions.

More information is available at https://zopetoolkit.readthedocs.io/.
