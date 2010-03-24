#!/bin/zsh
echo "Production"
rm *.pyc
ln -sf production_config.py localconfig.py
colordiff -u12 =(python ../mozilla2/config.py) =(python config.py)


echo "Staging"
rm *.pyc
ln -sf staging_config.py localconfig.py
colordiff -u12 =(python ../mozilla2-staging/config.py) =(python config.py)
