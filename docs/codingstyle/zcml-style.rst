ZCML
====

File naming conventions
-----------------------

ZCML configuration for a package should, in general, be placed in a file
named ``configure.zcml``.  If a package performs meta configuration
(defines new configuration directives), the meta configuration should go
in a file named ``meta.zcml``.  The code that implements the meta
configuration directives should (again, in general) go in a file named
``metaconfiguration.py``.


Style guide
-----------

The ZCML style guide has been developed with the following qualities in
mind:

* Lines under 80 characters wherever possible

* Indentation to reflect nesting

* Ease of maintenance

* Easy visual scanning through ZCML


Tabs and spaces
~~~~~~~~~~~~~~~

All whitespace to be made up of space characters. No chr(9) hard tabs.

Indentation of 2 characters to show nesting, 4 characters to list
attributes on separate lines. This distinction makes it easier to see
the difference between attributes and nested elements.


Logical sections
~~~~~~~~~~~~~~~~

If a configuration file has many logical sections, then mark the
sections with comments and indent the sections relative to the comments.
For example::

    <configure xmlns="http://namespaces.zope.org/zope">

      <!-- Configuration registries -->

      <content
          class="zope.app.services.configuration.ConfigurationRegistry"
          >
        <require
             permission="zope.ManageServices"
             interface="zope.app.interfaces.services.configuration.IConfigurationRegistry"
             />
      </content>

      <!-- Adapter Service -->

      <content class="zope.app.services.adapter.AdapterService">
        <implements

      ...


Namespaces
~~~~~~~~~~

Always use the "usual" names for namespaces in the document:

default (no qualification needed)
    for http://namespaces.zope.org/zope

browser
    for http://namespaces.zope.org/browser

zmi
    for http://namespaces.zope.org/zmi

security
    for http://namespaces.zope.org/security

xmlrpc
    for http://namespaces.zope.org/xmlrpc

whatevername
    for http://namespaces.zope.org/whatevername

Only define those namespaces used in the document. This is a similar
rule to what imports to use in a Python module.


Opening tags
~~~~~~~~~~~~

Close a one-line tag on the same line::

    <class class="Foo">

Close a multi-line tag on a new line, at the same level of indentation
as the tags attributes::

    <browser:pages
        name="index.html"
        class=".index.Index"
        >


Empty tags
~~~~~~~~~~

Close a one-line tag on the same line, insert a space after the last
attribute:::

    <subscriber handler=".foo.OnFoo" />

Close a multi-line tag on a new line at the same level of indentation as
the tag's attributes::

    <browser:page
        name="index.html"
        class=".index.Index"
        />


Closing tags
~~~~~~~~~~~~

Indent closing tags at the same level of indentation as the opening
tags::

    <class class=".foo.Foo">
        ...
    </class>

Attributes
~~~~~~~~~~

If all the attributes fit on one line with the tag name, do that::

    <class class=".foo.Foo">

If all the attribute fit on one line without the tag name, do that on
the line after the tag, indented 4 spaces along from the tag::

    <browser:page
        name="index.html" class=".foo.Foo" permission="zope.View"
        />

Otherwise, put the first attribute on a new line, and use one line per
attribute::

    <browser:page
        name="index.html"
        class=".foo.Foo"
        permission="zope.View"
        template="foo.pt"
        />

Use double quotes for attributes unless single quotes are needed to
enclose double quotes.


Comments
~~~~~~~~

Comments should be placed immediately above the declarations they apply
to. Keep comments to one line where possible, and open and close the
comment on the same line.
