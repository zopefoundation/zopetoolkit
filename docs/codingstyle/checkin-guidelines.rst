Check-in guidelines
===================

Please be careful before a check in to make sure:

 - All the code you are about to check in has reasonable test coverage.
   If you want to check in partial code in order to collaborate remotely,
   do so in a branch.

 - All the tests pass. Running individual tests for the code you are
   working on is fine while developing, but immediately before a check
   in, all tests must be run.

   Build environments based on buildout usually do so by running::

      bin/test --all

 - Use 'git status' to make sure you have added any new files to the
   repository.  Alternatively you could make a fresh checkout before running
   the tests.

 - Please be aware of the version of Python you use. The recommended and
   supported versions of Python vary over time (although they do so slowly).
