#!/bin/bash
#
# Script:
#   test-masters.sh
#
# Purpose:
#   This script will make sure that any changes on buildbot-configs
#   are valid. The script will call setup-master.py for each master
#   to make sure that they will be able to run 'buildbot checkconfig'.
#   This script defaults to checking 0.7.x masters, and will test
#   0.8.x masters when the -8 switch is passed.
#
# Requirements:
#   You have to have buildbot installed.
#   Include buildbotcustom and tools/lib/python in your PYTHONPATH.
#
# Author:
#   Chris AtLee <catlee@mozilla.com>
#
set -e
if [ -n "$TEMP" ]; then
    master_dir=$TEMP/master_dir
else
    master_dir=master_dir
fi
# $extra_args determines if you will iterate through the 0.8.x
# based masters or the 0.7.x ones
if [ "$1" = "-7" ]; then
    extra_args=-7

# Any other arg will be treated as a json file to load
elif [ -n "$1" ]; then
    extra_args="-j $1"
fi

exit_code=0

# Also test the simpler masters
for master_name in simple-talos; do
    echo -n "${master_name}... "
    (cd $master_name; buildbot checkconfig > /dev/null && echo OK)
done
# It will iterate through list of masters and checkconfig for each one of them
for master_name in $(python setup-master.py $extra_args --list); do
    rm -rf $master_dir
    mkdir $master_dir
    echo -n "${master_name}... "
    python setup-master.py $extra_args $master_dir $master_name
    (cd $master_dir; buildbot checkconfig > /dev/null && echo OK) || \
        { echo "Broken pieces are in $master_dir"; exit_code=1; false; }
    rm -rf $master_dir
done

exit $exit_code
