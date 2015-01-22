==========
2010-04-06
==========

This is the summary of the weekly Zope developer meeting which happened on
Tuesday, 2010-04-06 on #zope@irc.freenode.org from 3pm to 3:30pm (UTC).

The agenda for this meeting is available in the mailing list archives:
https://mail.zope.org/pipermail/zope-dev/2010-April/039981.html

The IRC logs are located here:
http://zope3.pov.lt/irclogs-zope/%23zope.2010-04-06.log.html#t2010-04-06T18:00:01

Tres Seaver was filling in for Christian Theune as conventer due to illness.


Zope2 release manager
---------------------

The community welcomes Hanno Schlichting as the new release manager for
Zope2.  In addition to closing / responding to dozens of bugs in the past
week, Hanno has also proposed a roadmap for Zope 2.13 and has made the
release tag for Zope 2.12.4.


Porting packages to Zope3
-------------------------

Lennart Regebro reported that he has branches waiting for the first three
"most depended-on" ZTK packages (``zope.event``, ``zope.interface``, and
``zope.testing``).  After considering naming the new releases ``4.0``,
the consensus was to just name them the next "normal" major release, as
long as there are no backward-incompatible API changes.

Some discussion of the general problem of doctests breaking due to exception
formatting led to a suggestion from Jim Fulton that we implement a testing
API similar the ``unittest.TestCase.assertRaises``, but with the additional
feature that it returns the exception value, to permit further assertions
about the state of that object.


Buildbots
---------

No one had new updates on the topic.  Sidnei da Silva reported that he
is close to reconstructing the script used to build ``win64`` images for
Amazon EC.

Tres Seaver reported that his request to Microsoft for dontaed VisualStudio
licnese to support builds / tests of ``zope.*`` packages on Windows
for Python 2.4 and 2.5 is still stalled.

Baiju M noted that Rackspace can also support Windows in its cloud:
http://www.rackspacecloud.com/ .


Tracker status
--------------

Charlie Clark reported that he had gotten his script for checking
Launchpad for "languishing" bugs working.  He posted that package to
``zope-dev@zope.org`` during the meeting.


Bug Days
--------

After some discussion, Adam Groszer and Baiju M agreed to widen their planned
``bluebream`` sprint to include more general ZTK issues.  The sprint,
originally set for Saturday, 2010-04-10, was rescheduled to Saturday,
2010-04-24.  Charlie Clark asked for announcments, plus volunteers willing
to help mentor new exterminators during the bug day.  Adam and Baiju will
organize a web page for coordinating the bug day activity, and send out
the announcements.


Carried Over
------------

- Resurrecting the "sprint schedule" page,
  http://wiki.zope.org/zope3/SprintSchedule

- A more general calendar (e.g., for Zope / Python related conferences,
  symposia, sprints, etc.)
