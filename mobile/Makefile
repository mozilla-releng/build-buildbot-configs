BUILDBOT=./bin/buildbot
PYTHONPATH=master
PYTHONHOME=.
#BuildID and ProductName are for local testing and shouldn't be checked in
#Example: 
#BUILDID=1287695122
PLATFORM=maemo5-gtk
MODEL=n900-gtk
BRANCH=mozilla-central
#Example:
#PRODUCT_NAME=fennec-4.0b2pre
CONFIG_BRANCH=default
CUSTOM_BRANCH=default

none:
	@echo Invalid

start:
	PYTHONHOME=$(PYTHONHOME) PYTHONPATH=$(PYTHONPATH) $(BUILDBOT) start `pwd`/master

stop:
	PYTHONHOME=$(PYTHONHOME) PYTHONPATH=$(PYTHONPATH) $(BUILDBOT) stop `pwd`/master

reconfig:
	PYTHONHOME=$(PYTHONHOME) PYTHONPATH=$(PYTHONPATH) $(BUILDBOT) reconfig master

checkconfig:
	PYTHONHOME=$(PYTHONHOME) PYTHONPATH=$(PYTHONPATH) $(BUILDBOT) checkconfig master/master.cfg

sendchange:
	python -c "assert '$(BUILDID)'.strip(), 'missing BUILDID var'"
	python -c "assert '$(PRODUCT_NAME)'.strip(), 'missing PRODUCT_NAME var'"
	PYTHONHOME=$(PYTHONHOME) PYTHONPATH=$(PYTHONPATH) $(BUILDBOT) sendchange \
	--master localhost:9010 \
	--user sendchange-$(MODEL)-$(BUILDID) \
	--branch $(BRANCH)-$(MODEL) \
	http://ftp.mozilla.org/pub/mozilla.org/mobile/tinderbox-builds/$(BRANCH)-$(PLATFORM)/$(BUILDID)/$(PRODUCT_NAME).en-US.linux-gnueabi-arm.tar.bz2

update:
	@python -c "print '='*80"
	@echo -n Updating Master `basename ${PWD}` | tee -a master.log
	@date | tee -a master.log
	@echo -n "buildbot-configs old rev: " | tee -a master.log
	@hg -R buildbot-configs identify >> master.log
	hg -R buildbot-configs pull -r $(CONFIG_BRANCH)
	hg -R buildbot-configs up -C
	@echo -n "buildbot-configs new rev: " | tee -a master.log
	@hg -R buildbot-configs identify >> master.log
	@echo -n "buildbotcustom old rev: " | tee -a master.log
	@hg -R buildbotcustom identify >> master.log
	hg -R buildbotcustom pull -r $(CUSTOM_BRANCH)
	hg -R buildbotcustom up -C
	@echo -n "buildbotcustom new rev: " | tee -a master.log
	@hg -R buildbotcustom identify >> master.log
	@echo Finished updating at `date` | tee -a master.log
