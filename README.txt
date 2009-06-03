=======================
Using a custom buildout
=======================

Note: If you are using Windows, if you do not have PIL installed, or you are
not using Python 2.4 as your main system Python, please see the relevant
sections below.

You probably got here by running something like:

 $ paster create -t plone3_buildout

Now, you need to run:

 $ python bootstrap.py

This will install zc.buildout for you.

To create an instance immediately, run:

 $ bin/buildout

This will download Plone's eggs and products for you, as well as other
dependencies, create a new Zope 2 installation (unless you specified
an existing one when you ran "paster create"), and create a new Zope instance
configured with these products.

You can start your Zope instance by running:

 $ bin/instance start

or, to run in foreground mode:

 $ bin/instance fg

To run unit tests, you can use:

 $ bin/instance test -s my.package

Installing PIL
--------------

To use Plone, you need PIL, the Python Imaging Library. If you don't already
have this, download and install it from http://www.pythonware.com/products/pil.

Using a different Python installation
--------------------------------------

Buildout will use your system Python installation by default. However, Zope
2.10 (and by extension, Plone) will only work with Python 2.4. You can verify
which version of Python you have, by running:

 $ python -V

If that is not a 2.4 version, you need to install Python 2.4 from
http://python.org. If you wish to keep another version as your main system
Python, edit buildout.cfg and add an 'executable' option to the "[buildout]"
section, pointing to a python interpreter binary:

 [buildout]
 ...
 executable = /path/to/python

Working with buildout.cfg
-------------------------

You can change any option in buildout.cfg and re-run bin/buildout to reflect
the changes. This may delete things inside the 'parts' directory, but should
keep your Data.fs and source files intact.

To save time, you can run buildout in "offline" (-o) and non-updating (-N)
mode, which will prevent it from downloading things and checking for new
versions online:

 $ bin/buildout -Nov

Creating new eggs
-----------------

New packages you are working on (but which are not yet released as eggs and
uploaded to the Python Package Index, aka PYPI) should be placed in src. You can do:

 $ cd src/
 $ paster create -t plone my.package

Use "paster create --list-templates" to see all available templates. Answer
the questions and you will get a new egg. Then tell buildout about your egg
by editing buildout.cfg and adding your source directory to 'develop':

 [buildout]
 ...
 develop =
    src/my.package

You can list multiple packages here, separated by whitespace or indented
newlines.

You probably also want the Zope instance to know about the package. Add its
package name to the list of eggs in the "[instance]" section, or under the
main "[buildout]" section:

 [instance]
 ...
 eggs =
    ${buildout:eggs}
    ${plone:eggs}
    my.package

Leave the ${buildout:eggs} part in place - it tells the instance to use the
eggs that buildout will have downloaded from the Python Package Index
previously.

If you also require a ZCML slug for your package, buildout can create one
automatically. Just add the package to the 'zcml' option:

 [instance]
 ...
 zcml =
    my.package

When you are finished, re-run buildout. Offline, non-updating mode should
suffice:

 $ bin/buildout -Nov

Developing old-style products
-----------------------------

If you are developing old-style Zope 2 products (not eggs) then you can do so
by placing the product code in the top-level 'products' directory. This is
analogous to the 'Products/' directory inside a normal Zope 2 instance and is
scanned on start-up for new products.

Depending on a new egg
----------------------

If you want to use a new egg that is in the Python Package Index, all you need
to do is to add it to the "eggs" option under the main "[buildout]" section:

 [buildout]
 ...
 eggs =
    my.package

If it's listed somewhere else than the Python Package Index, you can add a link
telling buildout where to find it in the 'find-links' option:

 [buildout]
 ...
 find-links =
    http://dist.plone.org
    http://download.zope.org/distribution/
    http://effbot.org/downloads
    http://some.host.com/packages

Using existing old-style products
---------------------------------

If you are using an old-style (non-egg) product, you can either add it as an
automatically downloaded archive or put it in the top-level "products" folder.
The former is probably better, because it means you can redistribute your
buildout.cfg more easily:

 [productdistros]
 recipe = plone.recipe.distros
 urls =
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz

If someproduct-1.3.tar.gz extracts into several products inside a top-level
directory, e.g. SomeProduct-1.3/PartOne and SomeProduct-1.3/PartTwo, then
add it as a "nested package":

 [productdistros]
 recipe = plone.recipe.distros
 urls =
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz
 nested-packages =
    someproduct-1.3.tar.gz

Alternatively, if it extracts to a directory which contains the version
number, add it as a "version suffix package":

 [productdistros]
 recipe = plone.recipe.distros
 urls =
    http://plone.org/products/someproduct/releases/1.3/someproduct-1.3.tar.gz
 version-suffix-packages =
    someproduct-1.3.tar.gz

You can also track products by adding a new bundle checkout part. It
doesn't strictly have to be an svn bundle at all, any svn location will do,
and cvs is also supported:

 [buildout]
 ...
 parts =
    plone
    zope2
    productdistros
    myproduct
    instance
    zopepy

Note that "myproduct" comes before the "instance" part. You then
need to add a new section to buildout.cfg:

 [myproduct]
 recipe = plone.recipe.bundlecheckout
 url = http://svn.plone.org/svn/collective/myproduct/trunk

Finally, you need to tell Zope to find this new checkout and add it to its
list of directories that are scanned for products:

 [instance]
 ...
 products =
    ${buildout:directory}/products
    ${productdistros:location}
    ${plonebundle:location}
    ${myproduct:location}

Without this last step, the "myproduct" part is simply managing an svn
checkout and could potentially be used for something else instead.

=============
Using Windows
=============

To use buildout on Windows, you will need to install a few dependencies which
other platforms manage on their own.

Here are the steps you need to follow (thanks to Hanno Schlichting for these):

Python (http://python.org)
--------------------------

  - Download and install Python 2.4.4 using the Windows installer from
    http://www.python.org/ftp/python/2.4.4/python-2.4.4.msi
    Select 'Install for all users' and it will put Python into the
    "C:\Python24" folder by default.

  - You also want the pywin32 extensions available from
    http://downloads.sourceforge.net/pywin32/pywin32-210.win32-py2.4.exe?modtime=1159009237&big_mirror=0

  - And as a last step you want to download the Python imaging library available
    from http://effbot.org/downloads/PIL-1.1.6.win32-py2.4.exe

  - If you develop Zope based applications you will usually only need Python 2.4
    at the moment, so it's easiest to put the Python binary on the systems PATH,
    so you don't need to specify its location manually each time you call it.

    Thus, put "C:\Python24" and "C:\Python24\Scripts" onto the PATH. You can
    find the PATH definition in the control panel under system preferences on
    the advanced tab at the bottom. The button is called environment variables.
    You want to add it at the end of the already existing PATH in the system
    section. Paths are separated by a semicolons.

  - You can test if this was successful by opening a new shell (cmd) and type
    in 'python -V'. It should report version 2.4.4 (or whichever version you
    installed).

    Opening a new shell can be done quickly by using the key combination
    'Windows-r' or if you are using Parallels on a Mac 'Apple-r'. Type in 'cmd'
    into the popup box that opens up and hit enter.


Subversion (http://subversion.tigris.org)
-----------------------------------------

  - Download the nice installer from
    http://subversion.tigris.org/files/documents/15/35379/svn-1.4.2-setup.exe

  - Run the installer. It defaults to installing into
    "C:\Program Files\Subversion".

  - Now put the install locations bin subfolder (for example
    "C:\Program Files\Subversion\bin") on your system PATH in the same way you
    put Python on it.

  - Open a new shell again and type in: 'svn --version' it should report
    version 1.4.2 or newer.


MinGW (http://www.mingw.org/)
-----------------------------

  This is a native port of the gcc compiler and its dependencies for Windows.
  There are other approaches enabling you to compile Python C extensions on
  Windows including Cygwin and using the official Microsoft C compiler, but this
  is a lightweight approach that uses only freely available tools. As
  it's used by a lot of people chances are high it will work for you and there's
  plenty of documentation out there to help you in troubleshooting problems.

  - Download the MinGW installer from
    http://downloads.sourceforge.net/mingw/MinGW-5.1.3.exe?modtime=1168794334&big_mirror=1

  - The installer will ask you which options you would like to install. Choose
    base and make here. It will install into "C:\MinGW" by default. The install
    might take some time as it's getting files from sourceforge.net and you
    might need to hit 'retry' a couple of times.

  - Now put the install location's bin subfolder (for example "C:\MinGW\bin") on
    your system PATH in the same way you put Python on it.

  - Test this again by typing in: 'gcc --version' on a newly opened shell and
    it should report version 3.4.2 or newer.


Configure Distutils to use MinGW
--------------------------------

  Some general information are available from
  http://www.mingw.org/MinGWiki/index.php/Python%20extensions for example but
  you don't need to read them all.

  - Create a file called 'distutils.cfg' in "C:\Python24\Lib\distutils". Open it
    with a text editor ('notepad distutils.cfg') and fill in the following lines:

    [build]
    compiler=mingw32

    This will tell distutils to use MinGW as the default compiler, so you don't
    need to specify it manually using "--compiler=mingw32" while calling a
    package's setup.py with a command that involves building C extensions. This
    is extremely useful if the build command is written down in a buildout
    recipe where you cannot change the options without hacking the recipe
    itself. The z2c.recipe.zope2install used in ploneout is one such example.
