TODO comments
=============

Occasionally you may need to note a place in a file that needs to be
revisited later. There are three standard codes used to designate such
places: ``XXX``, ``TODO``, and ``BBB``.

Depending on the type of the file, those codes should be placed
within a comment according to the applicable syntax.


XXX
  XXX comments should only be used during development to note things
  that need to be taken care of before a final (trunk) commit::

    # XXX This will break if someone types `9`.

  One should not expect to see XXX in released software.

  It should be extremely rare to check in an XXX on a trunk. If an
  XXX is checked in on a trunk:

  o The intention and expectation will be that someone will resolve
    the XXX before someone releases the code.

  o The XXX must fully describe an issue, so that someone else can
    read the comment and know what it's about.

  XXX shall not be used to record new features, non-critical
  optimization, design changes, etc.


TODO
  If you want to record things like new features, non-critical
  optimizations, design changes, or other long term changes, use
  TODO comments::

    # TODO This could go faster if we'd use a better data structure.

  People making a release shouldn't care about TODOs, but they ought to
  be annoyed to find XXXs.


BBB
  When adding code to preserve backward compatibility, use a BBB
  comment with a date. For example::

    # BBB 2016-07-08, preserves use of 'get_foo' function
