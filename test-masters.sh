#!/bin/bash
set -e
master_dir=master_dir
if [ "$1" = "-8" ]; then
    extra_args=-8
fi

exit_code=0

for master_name in $(python setup-master.py $extra_args -l); do
    rm -rf $master_dir
    mkdir $master_dir
    echo -n "${master_name}... "
    python setup-master.py $extra_args $master_dir $master_name
    (cd $master_dir; buildbot checkconfig > /dev/null && echo OK) || { echo "Broken pieces are in $master_dir"; exit_code=1; false; }
    rm -rf $master_dir
done

exit $exit_code
