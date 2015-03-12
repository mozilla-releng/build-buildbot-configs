#!/bin/bash
# This script has been rewritten in setup_master.py using
# the -t option.  We use that now
exit=0

# even though it isn't fully used, the config check does require a valid
# shared memory setup AT THE DEFAULT LOCATION. If you're running on a
# laptop, that may not exist. Fail early.
#
# OSX note: it "works" (for test-masters purposes) to just create the
#           directory, even though that isn't how shared memory is
#           handled on OSX. The directories must be owned by the id
#           running the tests.
#
# if you want to run trial tests without needing to execute the full test suite
# call this script with: run-test

shm=(/dev/shm)
good_shm=true
for needed_dir in ${shm[@]}; do
    if ! test -w $needed_dir; then
        echo 1>&2 "No shm setup, please create writable directory '$needed_dir'"
        good_shm=false
    fi
done
$good_shm || exit 1

WORK=test-output
mkdir $WORK 2>/dev/null


function run_unittests {
for dir in mozilla mozilla-tests; do
  cd $dir
  for f in test/*.py; do
    trial $f || exit=1
  done
  rm -rf _trial_temp
  cd ..
done
}

if [ "$1" == "run-tests" ]
then
    # run trial and exit
    run_unittests
    exit
fi

actioning="Checking"
MASTERS_JSON_URL="${MASTERS_JSON_URL:-https://hg.mozilla.org/build/tools/raw-file/tip/buildfarm/maintenance/production-masters.json}"

atexit=()
trap 'for cmd in "${atexit[@]}"; do eval $cmd; done' EXIT

# I have had problems where a whole bunch of parallel HTTP requests caused
# errors (?), so fetch it once here and pass it in.
MASTERS_JSON=$(mktemp $WORK/tmp.masters.XXXXXXXXXX)
curl -q -o$MASTERS_JSON "$MASTERS_JSON_URL" || exit 1
atexit+=("rm $MASTERS_JSON")

FAILFILE=$(mktemp $WORK/tmp.failfile.XXXXXXXXXX)
atexit+=("rm $FAILFILE")

# Construct the set of masters that we will test.
MASTERS=($(./setup-master.py -l -j "$MASTERS_JSON" --tested-only "$@"))

# Fire off all the tests in parallel.
for MASTER in ${MASTERS[*]}; do (
    OUTFILE=$(mktemp $WORK/tmp.testout.XXXXXXXXXX)

    ./setup-master.py -t -j "$MASTERS_JSON" "$@" $MASTER > $OUTFILE 2>&1 || echo "$MASTER" >> $FAILFILE
    cat $OUTFILE # Make the output a little less interleaved
    rm $OUTFILE
) &
atexit+=("[ -e /proc/$! ] && kill $!")
done

echo "$actioning ${#MASTERS[*]} masters..."
echo "${MASTERS[*]}"
wait

check_for_virtual_env() {
    if test -z "$VIRTUAL_ENV"; then
        echo "NOTE: you were not using a virtual environment" 1>&2
    fi
}

if [ -s $FAILFILE ]; then
    echo "*** $(wc -l < $FAILFILE) master tests failed ***" >&2
    echo "Failed masters:" >&2
    sed -e 's/^/  /' "$FAILFILE" >&2
    check_for_virtual_env
    exit 1
fi

run_unittests

if test "$exit" -ne 0 ; then
    check_for_virtual_env
fi

exit $exit
