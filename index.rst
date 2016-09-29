.. This document contains release-specific information about the Zope Toolkit.
   It is intended for automatic inclusion by the ZTK sphinx-based
   documentation.


Introduction
------------

The Zope Toolkit is a collection of libraries managed together by the
Zope developers. We typically treat each library independently, so you
should look at the CHANGES file in each library for updates.

Installation
------------

The Zope Toolkit cannot be installed directly except as individual
libraries (such as ``zope.component``). To install it you typically
would install a framework or application that makes use of these
libraries. Examples of such projects are Grok and Zope.

If you want to use the Zope Toolkit Known-Good-Set (KGS), you should
copy the ztk-versions.cfg file into your own project and include it
in your buildout via the extends mechanism.

Frameworks and applications have their own set of install instructions.
You should follow these in most cases.

Python versions
---------------

The ZTK supports Python 2.7, 3.3, 3.4 and 3.5.
