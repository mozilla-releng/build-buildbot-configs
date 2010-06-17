#!/bin/zsh
echo "Production"
rm *.pyc
ln -sf production_config.py localconfig.py
colordiff -u12 =(python ../mozilla2/config.py $1) =(python config.py $1)


echo "Staging"
rm *.pyc
ln -sf staging_config.py localconfig.py
colordiff -u12 =(python ../mozilla2-staging/config.py $1) =(python config.py $1)
