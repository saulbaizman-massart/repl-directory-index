#!/bin/sh
#
# DO NOT DELETE THIS FILE.
#
# Download and run directory-list.py from GitHub.
#

SELF=${0##*/}
WGET=$(which wget)
PYTHON=$(which python)
RM=$(which rm)
DIRECTORY_LIST=directory-list.py
GITHUB_USER=saulbaizman-massart
GITHUB_REPO=repl-directory-index
GITHUB_BRANCH=master
DOWNLOAD_URL=https://raw.githubusercontent.com/${GITHUB_USER}/${GITHUB_REPO}/${GITHUB_BRANCH}/${DIRECTORY_LIST}

echo
echo Starting ${SELF}...

# download latest version of program
echo
echo Downloading latest version of ${DIRECTORY_LIST} from ${DOWNLOAD_URL}...
echo ${WGET} -O ${DIRECTORY_LIST} ${DOWNLOAD_URL}
${WGET} -O ${DIRECTORY_LIST} ${DOWNLOAD_URL}

# run python program
echo
echo Running ${DIRECTORY_LIST} to generate repl toc...
echo ${PYTHON} ${DIRECTORY_LIST}
${PYTHON} ${DIRECTORY_LIST}

# delete python program
echo
echo Deleting ${DIRECTORY_LIST}... 
echo ${RM} -f ${DIRECTORY_LIST}
${RM} -f ${DIRECTORY_LIST}

echo
echo ...done.
echo