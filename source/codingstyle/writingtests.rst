Writing tests
=============

For any module 'somepkg.somemod' there should be a corresponding
unit test module 'somepkg.somemod.tests.testSomemod'.  Or if more than one
set of unit tests is desired, multiple test modules of the form
'somepkg.somemod.tests.testSomemodYYYY'.  Note that this means
that your 'somemod' directory needs to have a 'tests' subdirectory,
and that that subdirectory must have a (normally empty) '__init__.py'
file in it.

The file 'ut.py' in the root directory of the Z3 tree contains
a skeleton file appropriate for using in building unit test
modules.  If you use ut.py and follow the guidelines above,
then your unit tests will automatically be run when 'test.py'
is run.

In your unit test class, begin all unit test methods with the string 
'test'.
If you use the !CleanUp class support (see the comments in 'ut.py'),
make sure that your 'setUp' and 'tearDown' methods call the
!CleanUp class's 'setUp' and 'tearDown' methods::

    class TestSomething(CleanUp):
        def setUp(self):
            CleanUp.setUp(self)
            #your setup here

        def tearDown(self):
            #your teardown here
            CleanUp.tearDown(self)

**Never** give your test methods a docstring!  Doing so makes it very difficult
to find your test method when using the verbose output.  Use a comment instead.

Call your test class TestSomething, never just Test.

Call your test methods test_something(), not testSomething()

The typical approach to structuring the tests themselves is
to write test methods that exercise each individual method of
the class.  It is a good idea to organize these tests according to
the Interfaces implemented by the class under test.  In fact, it
is often best to implement such tests in separate mixin classes,
one class per Interface.  WritingInterfaceTests expands
on this concept in more detail.

Within the unit tests themselves, the Zope3 style is to use
the positive rather than the double negative assertions.
Thus, use ``assertEqual`` rather than ``failUnlessEqual``, 
``assertRaises`` rather than ``failUnlessRaises``, and ``assert_``
rather than ``failUnless``.  (Yes, ``assert_`` is an ugly name,
but it is still preferred.)

There are certain other "Best Practices" the following of which
leads to more robust and general unit tests:

  * If at all possible, avoid writing to the file system.  It should
    be possible to run the tests with only read-only access to
    the test directories.  If you do have to create files,
    create them using the python tempfile module.  Be sure to clean up
    after yourselves in your tearDown method.

  * It has been suggested that doing import of the module
    under test in the global section of the test module is bad,
    because in some uses of unittest test modules that generate
    import errors outside the tests themselves are ignored silently.
    It has also been suggested that if so this is a bug in unittest.
    I'm not aware of a definitive answer to this question.  If you
    wish to avoid globally importing the module under test, you
    can write a "helper function" to do the import and create and
    return instance(s) of the objects needed for testing,
    and call it from the start of each unit test.

Other Best Practices suggestions welcome!

