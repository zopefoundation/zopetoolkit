Zope Toolkit
============

The Zope Toolkit (ZTK) is a set of libraries intended for reuse by
projects to develop web applications or web frameworks. It is developed
by the contributors of the Zope Foundation.

The whole collection of ZTK libraries are used in various web
frameworks and web application servers, two examples of these are
Grok and Zope. If you install one of these systems, you will get a
part of the ZTK along with it automatically.

Installation
------------

The Zope Toolkit cannot be installed directly except as individual
libraries (such as ``zope.component``). To install it you typically
would install a framework or application that makes use of these
libraries.

If you want to use the Zope Toolkit Known-Good-Set (KGS), you should
copy the
`ztk-versions.cfg <https://github.com/zopefoundation/zopetoolkit/blob/master/ztk-versions.cfg>`_
file into your own project and include it in your buildout
via the extends mechanism.

Frameworks and applications have their own set of install instructions.
You should follow these in most cases.

Python versions
---------------

ZTK supports CPython 3.9, 3.10, 3.11, 3.12, 3.13 and PyPy3.


Documentation
-------------

.. toctree::
   :maxdepth: 2

   about
   process/index
   releases/index
   codingstyle/index
   attic/index
