#!/bin/bash -e
[ -z "${1}" ] || [ -z "${2}" ] && exit 1
TOX_INI_DIR="${1}"
TOX_WORK_DIR="${2}"

function hgme {
    repo="${1}"
    if [ ! -d "${TOX_WORK_DIR}/${repo}" ]; then
        hg clone https://hg.mozilla.org/build/${repo} "${TOX_WORK_DIR}/${repo}"
    else
        # this is equivalent to hg purge but doesn't require the hg purge plugin to be enabled
        hg status -un0 -R "${TOX_DIR}/${repo}" | xargs --no-run-if-empty --null rm -rf
        hg pull -u -R "${TOX_WORK_DIR}/${repo}"
    fi
}

hgme tools
hgme buildbotcustom
hgme buildbot
hgme braindump

hg -R "${TOX_WORK_DIR}/buildbot" checkout production-0.8
cd "${TOX_WORK_DIR}/buildbot/master" && python setup.py install
rm -rf "${TOX_INI_DIR}/test-output"
rm -rf "${TOX_INI_DIR}/run/shm/buildbot"
mkdir -p "${TOX_INI_DIR}/run/shm/buildbot"
cd ${TOX_INI_DIR} && "${TOX_WORK_DIR}/braindump/buildbot-related/dump_allthethings.sh"
