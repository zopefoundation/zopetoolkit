Toolkit libraries
=================

The Zope Toolkit consists of a set of libraries, which are commonly used by the
three major Zope frameworks (BlueBream, Grok and Zope 2).

Only a small subset of libraries from the Zope community are part of the
Toolkit. The Toolkit is in principle not limited to libraries from Zope
community.

Toolkit libraries
-----------------

The Toolkit libraries are standalone libraries which have their own releases,
bug trackers and in some cases active developer communities around them. The
toolkit acts as an umbrella project to deal with aspects which span multiple
of these libraries or have impacts on the major Zope frameworks.

The set of libraries that is part of the Toolkit can change over time depending
on how these libraries evolve and are used. New libraries considered for
inclusion can be added to the set, and existing libraries no longer used can be
removed from the set.

So the set of Zope Toolkit libraries is not static; what is included
continuously evolves. The project maintains a list of which libraries are part
of the Toolkit.

The Zope Toolkit Release Team is the final arbiter of which libraries are in
Zope Toolkit or not. It will generally make decisions according to these
loose guidelines:

* if all three framework use it, it's likely included.

* if it is in use in most applications build on top of all frameworks it's
  likely included.

* if it's used by only a single consumer platform, it's likely not included.

* if only a few people use it, it's likely not included.

* if it contains specific user interface code, it's likely not included. If it
  contains code to help construct user interfaces however, it can be included.

Libraries may have a different status in the Toolkit to convey extra information
about them, such as deprecation status.

Reasons to consider refactoring packages, making dependencies optional or
removing a library from the ZTK are:

* if a library contains specific user interface code this makes it a candidate
  for splitting it into a reusable non-UI part and a UI part that is outside of
  the toolkit. If a library is UI focused it makes it a candidate for removal
  from the toolkit.

* if a library doesn't have narrative documentation and there is no commitment
  from maintainers to create such documentation. Naturally critical libraries
  with a lot of use won't just be removed for this reason, but this should also
  be a good motivator to add documentation.

* if a library depends on another library maintained in the Zope repository that
  is itself not in the Toolkit we should think about removing this dependency or
  making the dependency optional. Another possibility is to remove the library
  that has this dependency from the toolkit altogether, or to adopt the
  dependency itself into the toolkit.

Community libraries
-------------------

Surrounding the Zope Toolkit libraries a large number of other libraries exists.
These libraries might integrate with the Zope Toolkit and might make use of the
Zope Toolkit.

The Zope Toolkit is not concerned with these community libraries and the release
team *does not* control the development of these libraries.
