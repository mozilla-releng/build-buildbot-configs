#!/bin/bash
# This script has been rewritten in setup_master.py using
# the -t option.  We use that now
exit=0

WORK=test-output
mkdir $WORK 2>/dev/null

actioning="Checking"
MASTERS_JSON_URL="${MASTERS_JSON_URL:-http://hg.mozilla.org/build/tools/raw-file/tip/buildfarm/maintenance/production-masters.json}"

atexit=()
trap 'for cmd in "${atexit[@]}"; do eval $cmd; done' EXIT

# I have had problems where a whole bunch of parallel HTTP requests caused
# errors (?), so fetch it once here and pass it in.
MASTERS_JSON=$(mktemp $WORK/tmp.masters.XXXXXXXXXX)
wget -q -O$MASTERS_JSON "$MASTERS_JSON_URL" || exit 1
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

for dir in mozilla mozilla-tests; do
  cd $dir
  for f in test/*.py; do
    trial $f || exit=1
  done
  rm -rf _trial_temp
  cd ..
done

if test "$exit" -ne 0 ; then
    check_for_virtual_env
fi

exit $exit
