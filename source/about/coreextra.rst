Core and Extra concepts
=======================

Introduction
------------

The Zope Framework covers only some libraries in the wider Zope
community and software repository. We introduce the concepts of *core*
and *extra* to be able to distinguish between the two.

Core libraries 
--------------

The Zope Framework is a set of libraries. These libraries are released
independently, but typically build on each other.

A library that at some point in time is considered to be part of the
Zope Framework is called a "core library". The Zope Framework contains
those libraries that are reused by a large number of projects, or that
the Zope Framework developers want to promote to be being more widely
adopted. The Zope Framework developers especially favor inclusions of
libraries that are used by other Zope projects.

The set of libraries that is "core" can change over time depending on
how these libraries evolve and are used. New libraries considered to
be "core" can be added to the set, and existing libraries once
considered "core" can be removed from the set.  We should be careful
though, as we cannot just drop libraries from the core without
considerable thought. A library being in the core signals a level of
commitment to this library.

How do we determine which libraries are part of the Zope Framework,
and which libraries are not? The set of Zope Framework libraries is
not static; what is included continuously evolves. The project
maintains a list of which libraries are considered core.

The Zope Framework Steering Group is the final arbiter of which
libraries are in Zope Framework or not. It will generally make decisions
according to these loose guidelines:

* if it's used widely in our community by the different consumer
  platforms, it's likely core.

* if it's used by only a single consumer platform, it's likely not
  core.

* if only a few people use it, it's likely not core.

* if it has a lot of people who contribute to it from our community,
  it's likely core.

* if it's something we want to encourage more consumer platforms use,
  it's likely core.

* if it contains specific user interface code, it's likely not
  core. If it contains code to help construct user interfaces however,
  it can be core.

Libraries may have a different status in the core to convey extra
information about them, such as deprecation status.

Extra libraries
---------------

Surrounding the Zope Framework core libraries a large number of other
libraries exist that are developed in association with the Zope
Framework. These libraries integrate with the Zope Framework and make
use of the Zope Framework. They are often maintained by developers
that are also Zope Framework developers, and similar development
practices are used.

We will call these libraries "extra". Libraries in the extra group are
sometimes candidates for inclusion in the core, or might be libraries
formerly part of the core but still being maintained. In general some
development philosophies and practices will be shared between the core
and extra group of libraries.

The Zope Framework steering group *does* not control the development
of the extra libraries in the repository, except where such a library
is considered for adoption within the Zope Framework itself as a core
library.

Examples of "extra" libraries are the "hurry.query" library for
constructing catalog queries, the "z3c.form" related libraries for
form generation, and the "grokcore.component" library which contains a
different way to configure components.

Any library that is developed for integration with the Zope Framework
in the Zope repository can be considered "extra"; "extra" is the set
of libraries that is not in the Zope Framework but can work with it. By 
having an "extra" designation we can more easily discuss such libraries.
