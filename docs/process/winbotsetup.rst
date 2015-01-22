.. _winbotdetails:

winbot details
==============

The whole service is a buildbot, reachable at http://winbot.zope.org.

It's tasks are:

  * Build windows binary eggs

    * Build is scheduled now every 30 minutes.

  * Test projects on windows

    * Nightly builds only


Building windows binary eggs
============================

A overview how it works:

* It gets all the released versions from pypi with an xmlrpc query
  (with the method package_releases).

* Optionally filters the versions (See the specs for
  version/platform constraints)

* Checks if there are binary eggs present for the various versions/platforms.

* If one is missing, builds it and uploads to pypi (setup.py bdist_egg),
  taking the source from the svn tag.

Developers interaction
----------------------

* Just upload your package version to pypi with `python setup.py sdist`,
  winbot is going to take care of the rest.

* Results can be checked either on pypi (that the eggs appear), or directly with
  winbot.
  Sample results: http://winbot.zope.org/builders/wineggbuilder/builds/60/steps/release%20eggs/logs/stdio
  Scroll to the bottom to see the summary table.

If you need a NEW package to be processed contact:

* Adam Groszer (agroszer-at-gmail-dot-com) or

* Hanno Schlichting (hanno-at-hannosch-dot-eu)

The package that creates the eggs is here:
svn://svn.zope.org/repos/main/zope.wineggbuilder


Detailed winbot configuration description
=========================================

Windows basics
--------------

  * kill unneeded services

    * ALG
    * Automatic Updates (yes!)
    * Computer Browser
    * DHCP Client
    * Print Spooler
    * Remote Registry
    * Server
    * TCP/IP NetBIOS Helper
    * Wireless Configuration

  * Windows firewall

    * kill file and printer sharing on all interfaces
    * allow only RDP, http, https

  * time sync

  * windows update (manual)

    * we should have only security updates, no fancy IE8 etc
    * better dont touch HW (this is VM)
    * restart, repeat windows update
    * kill off all c:\\windows\\$NtUninstall*, $hf_mig too

  * automatic windows update is OFF! (I hate when it f..s up the system)

  * download: (all downloaded stuff goes into c:\\install)

    * firefox
    * freecommander (my personally preferred stuff)
    * programmers notepad (my personal preferred stuff)
    * mydefrag
    * collabnet svn client
    * pythons 2.4 ... 2.7
    * pywin32
    * setuptools
    * mingw32
    * MS Visual C++ 2008 Express Edition
      http://www.microsoft.com/express/downloads/

pythons + pywin32 + setuptools
------------------------------

  * c:\\python24_32 NOT default
  * c:\\python25_32 NOT default

    * the trick is to install python25_sys+pywin32+setuptools first
      then copy c:\\python25_sys to python25_32

  * c:\\python26_32 NOT default
  * c:\\python26_64 NOT default

    * setuptools trick:
      get the source tgz, patch it with
      http://bugs.python.org/setuptools/issue2

  * c:\\python27_32 NOT default
  * c:\\python27_64 NOT default

    * setuptools trick: install setuptools from the patched source
      with setup.py install

  * c:\\python25_sys (default, 32bit, add to path)
  * clean versions of all the various pythons:

    * make a copy of the folder with the name `_clean` added
    * remove all traces of setuptools

      * from `site-packages`
      * from `scripts`

    * (or make a copy before installing setuptools -- I had all installed
      and did not want to install from scratch again)

  * install mingw32 to C:\\MinGW
  * collabnet svn client to C:\\svn
  * MSVC

    * check that build_ext works only with --compiler:
        * mingw32 fails because it's not on path
        * MSVC fails because ENV vars are missing

    * x64 sucks, but use this link:
        * http://www.mathworks.com/support/solutions/en/data/1-6IJJ3L/index.html?solution=1-6IJJ3L

  * create the ``buildbot`` user
  * create own user/other devs

    * setup .buildout (c:\\Documents and Settings\\<username>\\.buildout\\default.cfg) ::
      (everyone, please SHARE c:\\eggs, the disk is small)

    [buildout]
    eggs-directory=c:\\eggs

  * create user on PYPI: zope.wineggbuilder

    * grant perm to packages
    * what's up with ZODB3??? ask Jim
    * setup .pypirc

  * setup buildbot

    * http://buildbot.net/trac/wiki/RunningBuildbotOnWindows
    * grant permissions to user buildbot
    * beat it until it works (permissions, etc....)

  * put an apache in front of the whole

Buildbot for tests
------------------

Create a file called 'distutils.cfg' in
"C:\\Python24_32\\Lib\\distutils",  "C:\\Python25_32\\Lib\\distutils" ::

  [build]
  compiler=mingw32


Create a file called 'setupcompilerandexecute.bat' in
"C:\\Python24_32", "C:\\Python25_32" ::

  set PATH=%PATH%;c:\\mingw\\bin
  %*


Create a file called 'setupcompilerandexecute.bat' in
"C:\\Python26_32", "C:\\Python27_32" ::

  call "C:\\Program Files (x86)\\Microsoft Visual Studio 9.0\\VC\\VCVARSALL.bat" x86
  set PATH=%PATH%;"C:\\Program Files\\Microsoft SDKs\\Windows\\v6.1\\Bin"
  %*

Create a file called 'setupcompilerandexecute.bat' in
"C:\\Python26_64", "C:\\Python27_64" ::

  call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\bin\VCVARSX86_AMD64.bat"
  set PATH=%PATH%;"C:\Program Files\Microsoft SDKs\Windows\v6.1\Bin\x64"
  %*

For `clean` pythons such 'setupcompilerandexecute.bat' is created ::

  call "C:\Program Files (x86)\Microsoft Visual Studio 9.0\VC\VCVARSALL.bat" x86
  set PATH=%PATH%;"C:\Program Files\Microsoft SDKs\Windows\v6.1\Bin"
  rem make zc.buildout happy:
  set PYTHON2.4=c:\Python24_32_clean\python.exe
  set PYTHON2.5=c:\Python25_32_clean\python.exe
  set PYTHON2.7=c:\Python27_32_clean\python.exe
  %*

for the rest see master.cfg