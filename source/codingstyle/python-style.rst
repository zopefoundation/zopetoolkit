Python
======

The general rule when writing Python code is to follow PEP 8. The rules
given later in this document override what is said in `PEP 8`_.

Be tolerant of code that doesn't follow these conventions: our code base
has been evolving over years and doesn't always match the current style
as we update these rules.  Also, we want to reuse software written for
other projects that do not adhere to our rules.

Remember that PEP 8 explicitly allows breaking a rule in the interest of
keeping code consistent.

A reasonable goal is that code covered by the ZPL should follow these
conventions.


License statement, module docstring
-----------------------------------

Python files should always contain the most actual license comment at the top followed by the
module documentation string.

The docstring should contain a reference about version control status.
The example given is valid for at least CVS and Subversion.

Here is the template::

  ##############################################################################
  #
  # Copyright (c) 2009 Zope Corporation and Contributors.
  # All Rights Reserved.
  #
  # This software is subject to the provisions of the Zope Public License,
  # Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
  # THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
  # WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
  # WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
  # FOR A PARTICULAR PURPOSE
  # 
  ##############################################################################
  """One-line summary goes here.

  Module documentation goes here.

  $Id$
  """

.. note::
    TODO We never finished discussing license years. When should the
    license year be updated? Do we have to enumerate individual years or
    is it ok to give ranges?

    Guido (around 2002) pointed out the FSF's rules. Those should be
    re-evaluated.

    Efge pointed out that in the US only the first year of publication needs to be given. (See http://www.loc.gov/copyright/circs/circ03.html).

    This also points out that we need an understanding of when code is
    published the first time. Can checking into a public repository can
    count as published? The FSF seemed to understand inclusions in
    release tarballs as publications.


Whitespace
----------

Trailing whitespace should not occur, nor should blank lines at the end
of files.


Import statements
-----------------

All imports should be at the top of the module, after the module
docstring and/or comments, but before module globals.

It is sometimes necessary to violate this to address circular import
pronlems. If this is the case, add a comment to the import section at
the top of the file to flag that this was done.

Order your imports by simply ordering the lines as `sort` would. Don't
create blocks of imports with additional empty lines as PEP 8 recommends.

.. note::
    TODO This rule has been recommended by Jim but hasn't been
    officially established.


Refrain from using relative imports.  Instead of::

    import foo # from same package

you can write::

    from Zope.App.ThisPackage import foo

.. note::
    TODO Clarify, clean up wording. I think we also avoid re-imports of
    symbols and most times prefer the ``import`` over the ``from`` form.

    Relative imports should be avoided, I'm not sure about the style 
    once we start getting real relative imports from Python.


Attribute and method names
--------------------------

The naming of attributes as recommended by PEP 8 is controversial. PEP 8
prefers ``attribute_name`` over ``attributeName``. Newer code tends to
prefer the use of underscores over camel case. However, Zope 3 has been
built originally with the latter rule and a lot of code still use this
meme.

Boolean-type attributes should always form a true-false-question,
typically using "has" or "is" as prefix. Example: ``is_required`` instead
of ``required``.

Method names should always start with a verb that describes the action.

Examples::

    good:
    first_name
    is_required
    execute_command()
    save()
    convert_value_to_string()

    bad:
    FirstName
    required
    command()
    string()


.. note::
    TODO This rule needs clarification.


Global variable names
---------------------

Public global variables names are spelled with CapitalizedWords, as in
``Folder`` or ``RoleService``.

An exception is made for global non-factory functions, which are
typically spelled with ``mixedCase``.

.. note::
    TODO This rule needs clarification. What is a global variable
    anyway? It's not a constant AFAICT.


Local variables
---------------

Single-letter variable names should be avoided unless:

 - Their meaning is extremely obvious from the context, and

 - Brevity is desireable

The most obviouse case for single-letter variables is for iteration
variables.


``try``/``except`` blocks
-------------------------

``try`` blocks should cover as little code as possible. ``except``
statements should match exceptions as specific as possible.

For example, if you are converting a value to an ``int``, and you want
to catch conversion errors, you need only catch ``ValueError``. Be sure
to do the minimum possible between your ``try:`` and ``except
ValueError:`` statements::

    try:
        int(x)
    except ValueError:
        ...

String handling
---------------

Use ``startswith`` and ``endswith`` because it is faster, cleaner and less
error-prone than comparing sliced strings::

    # Yes:
    if foo.startswith('bar'):
        ...
    if foo.endswith('.html'):
        ...

    # No:
    if foo[:3]=='bar':
        ...
    if foo[-5:]=='.html':
        ...

.. note::
    TODO: Is this rule already PEP 8?

When checking if a string is a string, keep in mind that it might be a
unicode string too! The ``basestring`` type matches both ``str`` and
``unicode`` objects::

    if isinstance(obj, basestring):
        ...

.. note::
    TODO Does PEP 8 talk about this already?

Type checks
-----------

Constructs like ``if type(obj) is type('')`` should be replaced using
``isinstance()``::

      # Yes:
      if isinstance(obj, int):
        ...

      # No:
      if type(obj) is type(1):
        ...
      if type(obj) is int:


Marker objects
--------------

Use instances of ``object`` if you need to construct marker objects (for
example when detecting default values).  Compare them using ``is`` as
recommended by PEP 8.

.. note::
    TODO This was recommended by Steve Alexander but hasn't been
    officially approved for inclusion. Clarify its status.

Interfaces
----------

Interface names adhere to PEP 8's naming of classes, except that they
are prefixed with a capital ``I``, as in ``IMagicThing``.

One function of interfaces is to document functionality, so be very
verbose with the documentation strings.

All public interfaces should go into a file called ``interfaces.py``.
"Public" interfaces are those that you expect to be implemented more
than once. Interfaces that are likely to be implemented only once, like
``IGlobalAdapterService``, should live in the same module as their
implementation.

.. note::
    TODO clarify whether the single/multiple implementation rule holds.

    TODO there has been discussion about whether imperative or
    present tense is to be preferred for describing interfaces. The
    discussion was not resolved.


.. _`PEP 8`: http://www.python.org/dev/peps/pep-0008/
