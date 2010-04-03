#!/bin/bash
BUILDBOT=`which buildbot`
TEMPCONFIG='config.py.b4'
if [[ -f ./buildbot ]] ; then
    BUILDBOT='./buildbot'
fi

if [[ -f config.py ]] ; then
    echo 'you had a config.py, moving to $TEMPCONFIG'
    mv config.py $TEMPCONFIG
fi

echo ''
echo '============================='
echo '= testing production config ='
echo '============================='
echo ''
ln -s config-production.py config.py
$BUILDBOT checkconfig master.cfg
rm config.py
echo ''
echo '============================='
echo '=   done with production    ='
echo '============================='
echo ''

echo ''
echo '============================='
echo '=  testing staging config   ='
echo '============================='
echo ''
echo 'testing staging config'
ln -s config-staging.py config.py
$BUILDBOT checkconfig master.cfg
rm config.py

if [[ -f $TEMPCONFIG ]] ; then
    echo 'you had a config.py before starting, moving back'
    mv $TEMPCONFIG config.py
fi
echo ''
echo '============================='
echo '=    done with staging      ='
echo '============================='
echo ''
