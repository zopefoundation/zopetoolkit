================
The Zope Toolkit
================

The Zope Toolkit is a set of libraries maintained by the Zope project for
building web frameworks and application servers.

This directory contains the definition of the Zope Toolkit in the file
`ztk.cfg`. It specifies the list of packages included in the ZTK and packages
which are under review for inclusion.

Also, specific versions have been tested together (including their
dependencies) and can directly be used with a buildout by specifying this file
via the `extends` mechanism.

To test the ZTK, run ``bin/test-ztk``. 

To generate dependency graphs for the ZTK, run ``bin/depgraph``. The
resulting SVN graphs will be in ``parts/depgraph``.

For details about the ZTK, please see http://docs.zope.org/zopetoolkit.
