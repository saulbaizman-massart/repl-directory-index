#!/bin/sh
#
# DO NOT DELETE THIS FILE.
#
# Download and run directory-list.py from GitHub.
#

SELF=${0##*/}
WGET=`which wget`
PYTHON=`which python`
RM=`which rm`
PROGRAM=directory-list.py
URL=https://raw.githubusercontent.com/saulbaizman-massart/repl-directory-index/master/${PROGRAM}

echo
echo Starting $SELF...

# download latest version of program
echo
echo Downloading latest version of ${PROGRAM} from ${URL}...
echo ${WGET} -O ${PROGRAM} ${URL}
${WGET} -O ${PROGRAM} ${URL}

# run python program
echo
echo Running ${PROGRAM} to generate repl toc...
echo ${PYTHON} ${PROGRAM}
${PYTHON} ${PROGRAM}

# delete python program
echo
echo Deleting ${PROGRAM}... 
echo ${RM} ${PROGRAM}
${RM} ${PROGRAM}

echo
echo ...done.
echo