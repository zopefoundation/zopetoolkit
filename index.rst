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
extends mechanism (replace 1.1a1 by the desired version)::

  [buildout]
  extends = http://download.zope.org/zopetoolkit/index/1.1a1/ztk-versions.cfg

You can also copy the file locally or additionally extend the
zopeapp-versions.cfg file from the same location.

Frameworks and applications have their own set of install instructions. You
should follow these in most cases.

News
----

TODO


Migration issues
----------------

TODO
