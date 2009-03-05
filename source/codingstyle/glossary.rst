Glossary
========

This is a list of some common words that should have the same meaning
throughout Zope.  It is not exhaustive.

ID
    The term 'id' should only be used when we are talking about an
    identifier that is unique in the context of some particular id
    scheme. Examples include

    * A social security number, unique within a country's social secuity
      bureaucracy

    * A user id consisting of an NT Domain and a username, unique within
      a Windows NT network

    * A user id, unique within a Windows NT Domain

    * A Windows NT domain, unique within a Windows network

    We could consider the name of an object within a container to be an
    id within the id scheme of that container, but this is not a
    particularly useful way of thinking. One reason is that to identify
    the container, we need to consider it as having an id within the id
    scheme of *its* container.

    Id schemes should really be well-known points of reference within a
    system.  So, the model of Services in Zope 3 fits; you look up a
    service by its id within the service manager id scheme.

Key
    We use an object's name to get it from within a container.  The
    container sees these names as 'keys', so from a container's point of
    view, a name functions as a key to look up an object.

    When we use the term 'key', we really mean "a name functioning as a
    key in the context of a container".

Manager
    1. A user that configures components, such as a SiteManager.

    2. An object that performs through the web configuration, such as a
       ServiceManager (which allows site managers to configure
       services.)

    Generally, the word 'manager' is inappropriate for objects that
    don't perform through-the-web configuration.  For example, global
    "service services" are not configurable through the web, but they
    were once called "service managers", and have now been renamed,
    since the name caused confusion with through-the-web configurable
    service managers.

Name
    Objects are given names to help us find them. An object may be found
    via more than one name. In Zope 3, we use names to guide the process
    of traversing from a container to a contained object.

ZCML
    Zope Configuration Markup Language. An XML-based language used to
    configure software components.

References
----------

Martin Fowler, "Analysis Patterns: reusable object models", Addison Wesley
1997. Chapter 5 "Referring to Objects" has a good discussion of names, ids
and id schemes.
