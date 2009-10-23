import itertools
import logging
import subprocess
import os.path
import sys

class HandledException(Exception):
    def __init__(self, exc=None):
        self.exception=exc


mypath=os.path.dirname(os.path.abspath(sys.argv[0]))
buildout=os.path.dirname(mypath)

sources = {}


def ReadPackageSources():
    global sources

    try:
        input=open(os.path.join(buildout, "etc", "sources"))
    except IOError, e:
        logging.error("Failed to open package sources list (%s): %s "
                      (e.filename, e.strerror))
        raise HandledException(e) 

    for (number, line) in zip(itertools.count(), input):
        line=line.split("#", 1)[0].strip()
        if not line:
            continue

        try:
            (package, source)=line.split()
            sources[package]=source
        except ValueError, e:
            logging.warn("Syntax error in package source list at line %d" % (number+1))


def GetFullPackageName(pkg):
    global sources

    if not sources:
        ReadPackageSources()

    if pkg in sources:
        return pkg

    options=[name for name in sources.keys() if pkg in name]
    if len(options)==1:
        logging.warning("Using %s for requested %s" % (options[0], pkg))
        return options[0]

    raise KeyError(pkg)


def UpdatePins():
    pinfile=os.path.join(buildout, "versions.cfg")

    try:
        input=open(os.path.join(buildout, "etc", "versions"))
    except IOError, e:
        logging.error("Failed to read package verions list (%s): %s "
                      (e.filename, e.strerror))
        raise HandledException(e) 

    versions={}
    for (number, line) in zip(itertools.count(), input):
        line=line.split("#", 1)[0].strip()
        if not line:
            continue

        try:
            (package, version)=line.split()
            versions[package]=version
        except ValueError, e:
            logging.error("Syntax error in versions list")
            raise HandledException(e)

    sources=os.listdir(os.path.join(buildout, "src"))

    try:
        output=open(pinfile+"~", "wt")
    except IOError, e:
        logging.error("Failed to create temporary file: %s "
                      (e.filename, e.strerror))
        raise HandledException(e) 

    seen=set()
    for line in open(pinfile, "rt"):
        line=line.strip()
        if "=" not in line:
            print >>output, line
            continue

        (package, version)=[x.strip() for x in line.split("=",1)]
        seen.add(package)
        if package not in sources:
            if package in versions and version!=versions[package]:
                logging.info("Changing version for %s from %s to %s" %
                        (package, version, versions[package]))
                version=versions[package]
            print >>output, "%s = %s" % (package, version)
        else:
            logging.info("Removing version pin for %s" % package)


    for (pkg,version) in versions.items():
        if pkg not in seen and pkg not in sources:
            logging.info("Adding version pin for %s" % pkg)
            print >>output, "%s = %s" % (pkg, version)

    output.close()
    try:
        os.rename(pinfile+"~", pinfile)
    except OSError, e:
        logging.error("Failed to update versions.cfg: %s" % e.strerror)
        raise HandledException(e)


def UpdateBuildout():
    logging.info("Running buildout to update instance")
    bin=os.path.join(buildout, "bin", "buildout")

    command=subprocess.Popen([bin], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    (_,stderr)=command.communicate()
    if command.returncode!=0:
        logging.error("Buildout failed. Errors reported:")
        logging.error(stderr)
        raise HandledException()


logging.basicConfig(level=logging.INFO, format="%(message)s")

