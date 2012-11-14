#!/bin/bash
# This script has been rewritten in setup_master.py using
# the -t option.  We use that now

./setup-master.py -t "$@"

for dir in mozilla mozilla-tests; do
  cd $dir
  exit=0
  for f in test/*.py; do
    trial $f || exit=1
  done
  rm -rf _trial_temp
  cd ..
done
exit $exit
