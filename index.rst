.. This document contains release-specific information about the Zope Toolkit.
   It is intended for automatic inclusion by the ZTK sphinx-based
   documentation.


Introduction
------------

The Zope Toolkit 1.1 release is the second feature release of the Zope
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
libraries. Examples of such projects are BlueBream, Grok and Zope 2.

If you want to use the Zope Toolkit KGS, you can use the buildout
extends mechanism (replace 1.1 by the desired version)::

  [buildout]
  extends = http://download.zope.org/zopetoolkit/index/1.1/ztk-versions.cfg

You can also copy the file locally or additionally extend the
zopeapp-versions.cfg file from the same location.

Frameworks and applications have their own set of install instructions. You
should follow these in most cases.

Python versions
---------------

The ZTK 1.1 release series aim to support Python 2.5 up to Python 2.7. However,
there is an issue with the `zope.proxy` package using Python 2.7 on 64-bit
machines. This issue should be resolved with the upcoming release of Python
2.7.2. See also http://bugs.python.org/issue10360.

Some libraries included in the ZTK support Python 3.1 or later. But as a whole
the ZTK supports no Python 3.x version yet.

News
----

Python versions
~~~~~~~~~~~~~~~

Python 2.4 is no longer supported by this version of the ZTK. Support for
Python 2.7 has been added.

ZODB 3.10
~~~~~~~~~

This ZTK version includes ZODB 3.10 instead of 3.9 as included in the 1.0
series. You can read more about the changes at
http://pypi.python.org/pypi/ZODB3/3.10.0#change-history.

zc.buildout 1.5
~~~~~~~~~~~~~~~

The buildout version has been updated to 1.5 from the former 1.4 series. This
release requires some changes to recipes, so make sure to update all recipes to
compatible versions or check their availability first. More detailed changes
can be found at http://pypi.python.org/pypi/zc.buildout/1.5.2#change-history.

zope.testing 3.10
~~~~~~~~~~~~~~~~~

In zope.testing 3.10 the `zope.testing.testrunner` package has been moved to
a standalone distribution called `zope.testrunner`. You need to adjust your
imports or use compatible versions of test runner recipes.
