================
The Zope Toolkit
================

The Zope Toolkit is a set of libraries maintained by the Zope project for
building web applications, web frameworks and application servers.

This directory contains the definition of the Zope Toolkit in the file
``ztk.cfg``. It specifies the list of packages included in the ZTK and
packages which are under review for inclusion.

Also, specific versions have been tested together (including their
dependencies) and can directly be used with a buildout by specifying this file
via the ``extends`` mechanism.

To test the ZTK, run ``bin/test-ztk``.

To generate dependency graphs for the ZTK, run ``bin/depgraph``. The
resulting SVN graphs will be in ``parts/depgraph``.

For details about the ZTK, please see http://docs.zope.org/zopetoolkit.

Transition support
------------------

The libraries now maintained in the Zope Toolkit were previously
organized differently. Much code now maintained as part of the Zope
Toolkit was originally part of a set of packages in the ``zope.app.``
namespace. This code could in the past only be used by importing from
``zope.app.*`` packages, but has since been extracted into ``zope.*``
libraries to make it more reusable, and to leave old largely unused
code behind in ``zope.app.*``.

If you are a developer of an application or a framework that makes use
of the libraries now maintained within the Zope Toolkit, you need a
way to transition your code to the Zope Toolkit. The first step would
be to use ``ztk.cfg``, but you likely still have imports to
``zope.app.*`` that you need to update. The ``zopeapp.cfg`` file allows
you to build and test your application during this conversion process.

The ``zopeapp.cfg`` package set is equivalent to the core ``ztk.cfg`` set,
in that it offers a controlled set of ZTK compatible ``zope.app.*`` packages.
To help you transition your code, you can update your ``buildout.cfg`` to
extend both ``ztk.cfg`` and ``zopeapp.cfg``.

After doing this, we highly recommend you to change your code's
imports from from ``zope.app.*`` to the new places in ``zope.*``
wherever possible. The package's changelogs should contain information
as to where things are moved.  If not, try inspecting the module you
are importing from - the equivalent imports to ``zope.*`` are likely
there.

It may be that you are not able to change all your imports to ``zope.*``.
We would like to hear from you where this is not possible. We are
deliberately leaving old UI code behind in ``zope.app.*``, but it may be
we need to extract some more code into a more reusable form.

The transition support and ``zope.app.*`` support is limited: the zopeapp
legacy support will be officially retired from the ZTK after january
1, 2011.

Unless maintainers step up for some of these packages, compatibility updates
for most of these packages will also likely end. You are of course still
free to use older versions, but we highly recommend you upgrade your code to
the ZTK to receive the benefits of our continued maintenance efforts.
