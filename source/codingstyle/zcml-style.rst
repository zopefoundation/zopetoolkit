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

File placement conventions
--------------------------

Anything outside of zope.app needs to be usable outside of the
application server. This means it should have no dependencies on
zope.app.  In addition, anything outside of zope.app should have mimimal
dependencies on other zope packages.

Therefore, there should be no ZCML in packages outside of zope.app and
zope.configure.

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

The rules for adding TODO comments apply.

.. note::
    TODO Insert sphinx reference to the TODO comment document.


Comprehensive examples
~~~~~~~~~~~~~~~~~~~~~~

Example one, good style::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        >

        <adapter
            factory=".AttributeAnnotations."
            provides=".IAnnotations."
            for=".IAttributeAnnotatable." 
            />

    </configure>

Example two, could be better::

    <configure
       xmlns="http://namespaces.zope.org/zope"
       xmlns:security="http://namespaces.zope.org/security"
       xmlns:zmi="http://namespaces.zope.org/zmi"
       xmlns:browser="http://namespaces.zope.org/browser"
       >

    <!-- Standard configuration directives -->
    <include package=".Configuration" file="configuration-meta.zcml" />
    <include package=".App" file="app-meta.zcml" />
    <include package=".I18n" file="i18n-meta.zcml" />
    <include package=".Publisher" file="publisher-meta.zcml" />
    <include package=".Event" file="event-meta.zcml" />
    <include package=".StartUp" file="startup-meta.zcml" />


    <!-- Standard Permissions -->

    <security:permission id="zope.View"
                         title="View"
                         />

    <security:permission id="zope.Security"
                         title="Change security settings"
                         />

    <security:permission id="zope.ManageContent" 
                         title="Manage Content"
                         />

    <security:permission id="zope.ManageBindings" 
                         title="Manage Service Bindings"
                         />

    <security:permission id="zope.ManageServices" 
                         title="Manage Services"
                          />

    <security:permission id="zope.ManageApplication" 
                         title="Manage Application"
                         />

    <!-- XXX What is this for? -->
    <security:permission id="zope.I18n" 
                         title="Manage Application"
                         />

    <!-- Configuration -->
    <include package=".App" file="app.zcml" />
    <include package=".I18n" file="i18n.zcml" />
    <include package=".Publisher" file="publisher.zcml" />
    <include package=".Event" file="event.zcml" />
    <include package=".StartUp" file="startup-registry.zcml" />


    </configure>

The second example could be rewritten taking into account:

* Only defining the namespaces that are used

* Better formatting of security permission declarations

* Using 2 space and 4 space indents, not 3 space.

Example two, rewritten::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:security="http://namespaces.zope.org/security"
        >

      <!-- Standard configuration directives -->
      <include package=".Configuration" file="configuration-meta.zcml" />
      <include package=".App" file="app-meta.zcml" />
      <include package=".I18n" file="i18n-meta.zcml" />
      <include package=".Publisher" file="publisher-meta.zcml" />
      <include package=".Event" file="event-meta.zcml" />
      <include package=".StartUp" file="startup-meta.zcml" />

      <!-- Standard Permissions -->
      <security:permission id="zope.View" title="View" />
      <security:permission id="zope.Security" title="Change security settings" />
      <security:permission id="zope.ManageContent" title="Manage Content" />
      <security:permission 
          id="zope.ManageBindings" title="Manage Service Bindings" 
          />
      <security:permission id="zope.ManageServices" title="Manage Services" />
      <security:permission
         id="zope.ManageApplication" title="Manage Application" 
         />

      <!-- XXX What is this for? -->
      <security:permission
          id="zope.I18n" title="Manage Application" 
          />

      <!-- Configuration -->
      <include package=".App" file="app.zcml" />
      <include package=".I18n" file="i18n.zcml" />
      <include package=".Publisher" file="publisher.zcml" />
      <include package=".Event" file="event.zcml" />
      <include package=".StartUp" file="startup-registry.zcml" />

    </configure>

Example three, could be better::

    <configure
       xmlns="http://namespaces.zope.org/zope"
       xmlns:security="http://namespaces.zope.org/security"
       xmlns:zmi="http://namespaces.zope.org/zmi"
       xmlns:browser="http://namespaces.zope.org/browser"
       >

      <browser:defaultView
         for="zope.i18n.interfaces.ITranslationService."
         name="index.html"
         />

      <browser:view 
         permission="zope.ManageServices" 
         for="zope.i18n.interfaces.ITranslationService."
         factory="zope.app.browser.i18n.translate.">

         <browser:page name="index.html" attribute="index" />

         <browser:page name="editMessages.html" attribute="editMessages" />

         <browser:page name="deleteMessages.html"
                       attribute="deleteMessages" 
                       />

         <browser:page name="addLanguage.html" attribute="addLanguage" />
         <browser:page name="addDomain.html" attribute="addDomain" />

         <browser:page name="changeEditLanguages.html" 
                       attribute="changeEditLanguages" />
         <browser:page name="changeEditDomains.html" 
                       attribute="changeEditDomains" />
         <browser:page name="changeFilter.html" 
                       attribute="changeFilter" />

         <browser:page name="deleteLanguages.html"
                       attribute="deleteLanguages" />
         <browser:page name="deleteDomains.html" attribute="deleteDomains" />

      </browser:view>

      <zmi:tabs for="zope.i18n.interfaces.itranslationservice">
        <zmi:tab label="Translate" action="@@index.html"/>
      </zmi:tabs>

    </configure>

Example three reformatted::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:zmi="http://namespaces.zope.org/zmi"
        xmlns:browser="http://namespaces.zope.org/browser"
        >

      <browser:defaultView 
          for="zope.i18n.interfaces.ITranslationService" name="index.html" />

      <browser:view 
          permission="zope.ManageServices" 
          for="zope.i18n.interfaces.ITranslationService"
          factory="zope.app.browser.i18n.Translate"
          >

        <browser:page name="index.html" attribute="index" />

        <browser:page name="editMessages.html" attribute="editMessages" />

        <browser:page name="deleteMessages.html" attribute="deleteMessages" />

        <browser:page name="addLanguage.html" attribute="addLanguage" />
        <browser:page name="addDomain.html" attribute="addDomain" />

        <browser:page
            name="changeEditLanguages.html" attribute="changeEditLanguages" 
            />
        <browser:page
            name="changeEditDomains.html" attribute="changeEditDomains"
            />
        <browser:page
            name="changeFilter.html" attribute="changeFilter" 
            />

        <browser:page name="deleteLanguages.html" attribute="deleteLanguages" />
        <browser:page name="deleteDomains.html" attribute="deleteDomains" />

      </browser:view>

      <zmi:tabs for="zope.i18n.interfaces.ITranslationService">
        <zmi:tab label="Translate" action="@@index.html"/>
      </zmi:tabs>

    </configure>

Example three reformatted again. Note how putting the attributes of
``browser:page`` declarations on a separate line visually separates them,
so we don't need so much vertical whitespace::

    <configure
        xmlns="http://namespaces.zope.org/zope"
        xmlns:zmi="http://namespaces.zope.org/zmi"
        xmlns:browser="http://namespaces.zope.org/browser"
        >

      <browser:defaultView 
          for="zope.i18n.interfaces.ITranslationService" name="index.html" />

      <browser:view 
          permission="zope.ManageServices" 
          for="zope.i18n.interfaces.ITranslationService"
          factory="Zope.I18n.Views.Browser.Translate."
          >

        <browser:page
            name="index.html"
            attribute="index" 
            />
        <browser:page
            name="editMessages.html"
            attribute="editMessages" 
            />
        <browser:page
            name="deleteMessages.html"
            attribute="deleteMessages" 
            />
        <browser:page
            name="addLanguage.html"
            attribute="addLanguage" 
            />
        <browser:page
            name="addDomain.html"
            attribute="addDomain" 
            />
        <browser:page
            name="changeEditLanguages.html"
            attribute="changeEditLanguages" 
            />
        <browser:page
            name="changeEditDomains.html"
            attribute="changeEditDomains" 
            />
        <browser:page
            name="changeFilter.html" 
            attribute="changeFilter" 
            />
        <browser:page
            name="deleteLanguages.html" 
            attribute="deleteLanguages" 
            />
        <browser:page
            name="deleteDomains.html" 
            attribute="deleteDomains" 
            />

      </browser:view>

      <zmi:tabs for="zope.i18n.interfaces.ITranslationService">
        <zmi:tab label="Translate" action="@@index.html"/>
      </zmi:tabs>

    </configure>
