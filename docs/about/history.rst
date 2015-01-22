History of the Zope Toolkit
===========================

The Zope Toolkit started as "Zope 3". Zope 3 was the intended successor to the
Zope 2 platform. It didn't work out that way. Zope 3 can be used alone, but Zope
2 is still alive and well, and in fact started to use some parts of the Zope 3
codebase. We also have the Grok project came along that reused Zope 3 to build a
related but separate web framework.

We realized that the term "Zope 3" was overloaded, meaning both the set of
libraries shared by Zope 2 and Grok, and the actual web application server with
a user interface that you can install. We therefore introduced the term Zope
Toolkit so we could think about this set of shared libraries independently and
manage them that way.

Then, Zope 3 as an application server was renamed to BlueBream during the same
period. What was previously called "Zope 3" now consists in three parts :

- the Zope Component Architecture (ZCA)
- the set of libraries called the Zope Toolkit (ZTK)
- the application server called BlueBream
