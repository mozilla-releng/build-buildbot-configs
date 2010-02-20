#!/bin/bash
set -e
newline='
'
IFS=$newline
master_dir=master_dir
for args in $(python setup-master.py -l); do
    rm -rf $master_dir
    mkdir $master_dir
    echo -n "${args}... "
    cmd="python setup-master.py $master_dir $args"
    eval $cmd
    (cd $master_dir; buildbot checkconfig > /dev/null && echo OK || (echo "Broken pieces are in $master_dir"; false))
    rm -rf $master_dir
done
