#!/bin/bash
# This script has been rewritten in setup_master.py using
# the -t option.  We use that now
exit=0

./setup-master.py -t "$@" || exit=1

for dir in mozilla mozilla-tests; do
  cd $dir
  for f in test/*.py; do
    trial $f || exit=1
  done
  rm -rf _trial_temp
  cd ..
done
exit $exit
