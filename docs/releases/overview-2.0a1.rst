.. This file is generated. Please do not edit manually or check in.


.. _overview-2.0a1:

Zope Toolkit 2.0a1
==================

This document covers major changes in this release that can lead to
backward-incompatibilities and explains what to look out for when updating.

.. This document contains release-specific information about the Zope Toolkit.
   It is intended for automatic inclusion by the ZTK sphinx-based
   documentation.


Introduction
------------

The Zope Toolkit 2.0 release is the third feature release of the Zope
Toolkit. The Zope Toolkit really is just a collection of libraries
managed together by the Zope developers. We typically treat each
library independently, so you would like to look at the CHANGES.txt in
each library for updates. Here we note larger changes, especially ones
that affect multiple libraries.

Installation
------------

The Zope Toolkit cannot be installed directly except as individual
libraries (such as ``zope.component``). To install it you typically
would install a framework or application that makes use of these
libraries. Examples of such projects are BlueBream, Grok and Zope.

If you want to use the Zope Toolkit KGS, you can use the buildout
extends mechanism (replace 2.0 by the desired version)::

  [buildout]
  extends = http://download.zope.org/zopetoolkit/index/2.0/ztk-versions.cfg

You can also copy the file locally if you want to avoid network access.

Frameworks and applications have their own set of install instructions. You
should follow these in most cases.

Python versions
---------------

The ZTK 2.0 release series supports Python 2.6, 2.7 and 3.3. Some libraries
included in the ZTK support Python 3.2.

News
----

Python versions
~~~~~~~~~~~~~~~

Python 2.5 is no longer supported by this version of the ZTK. Support for
Python 3.3 has been added.

ZODB 4
~~~~~~

This ZTK version includes ZODB 4 instead of 3.10 as included in the 1.1
series. You can read more about the changes at
https://pypi.python.org/pypi/ZODB#change-history

Note that the former ZODB3 distribution has been split up into multiple
distributions. You can now separately install BTrees, persistent, ZEO and
ZODB.

zc.buildout 2
~~~~~~~~~~~~~

The buildout version has been updated to 2 from the former 1.x series. This
release requires some changes to recipes, so make sure to update all recipes to
compatible versions or check their availability first. More detailed changes
can be found at https://pypi.python.org/pypi/zc.buildout/2.1.0#change-history

Deprecated zope.app
~~~~~~~~~~~~~~~~~~~

This version of the ZTK no longer provides compatibility guarantees for any
zope.app.* libraries. Maintenance of these libraries is outside of the scope
of the ZTK and is taken up by individuals and framework developers.



List of packages
----------------

.. toctree::
   :maxdepth: 1

   packages-2.0a1

