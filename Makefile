package=pi
pyenv=ENV2
UNAME=$(shell uname)
VERSION=`head -1 VERSION`

define banner
	@echo
	@echo "###################################"
	@echo $(1)
	@echo "###################################"
endef

ifeq ($(UNAME),Darwin)
define terminal
	echo "Linux not yet supported, fix me"
endef
endif
ifeq ($(UNAME),Linux)
define terminal
	echo "Linux not yet supported, fix me"
endef
endif
ifeq ($(UNAME),Windows)
define terminal
	echo "Windows not yet supported, fix me"
endef
endif

clean:
	rm -rf *.zip
	rm -rf *.egg-info
	rm -rf *.eggs
	rm -rf docs/build
	rm -rf build
	rm -rf dist
	find . -name '__pycache__' -delete
	find . -name '*.pyc' -delete
	rm -rf .tox
	rm -f *.whl


######################################################################
# PYPI
######################################################################

todo:
 	sudo apt-get update
	sudo apt-get install emacs -y
	cd /home/pi/Desktop
	sudo git clone https://github.com/DexterInd/GrovePi
	cd /home/pi/Desktop/GrovePi/Script
	sudo chmod +x install.sh
	sudo ./install.sh
	sudo reboot


install-driver:
	sudo apt-get update
	sudo apt-get install emacs -y
	cd /home/pi/Desktop
	sudo git clone https://github.com/DexterInd/GrovePi
	cd /home/pi/Desktop/GrovePi/Script
	sudo chmod +x install.sh
	sudo ./install.sh
	sudo reboot

install-grovepi:
	sudo pip install grovepi
	sudo reboot -h now

######################################################################
# PYPI
######################################################################


dist: clean
	@echo "######################################"
	@echo "# $(VERSION)"
	@echo "######################################"
	# python setup.py sdist --formats=gztar,zip
	# python setup.py bdist
	python setup.py bdist_wheel

upload_test:
	python setup.py	 sdist bdist bdist_wheel upload -r https://testpypi.python.org/pypi

log:
	gitchangelog | fgrep -v ":dev:" | fgrep -v ":new:" > ChangeLog
	git commit -m "chg: dev: Update ChangeLog" ChangeLog
	git push

register: dist
	@echo "######################################"
	@echo "# $(VERSION)"
	@echo "######################################"
	* twine upload dist/*
	# twine register dist/cloudmesh.$(package)-$(VERSION)-py2.py3-none-any.whl
	# twine register dist/cloudmesh.$(package)-$(VERSION).tar.gz
	# twine register dist/cloudmesh.$(package)-$(VERSION).zip

upload: dist
	# twine upload dist/*
	twine upload dist/cloudmesh.$(package)-$(VERSION)-py2.py3-none-any.whl
	# twine upload dist/cloudmesh.$(package)-$(VERSION).tar.gz
	# twine upload dist/cloudmesh.$(package)-$(VERSION).zip

#
# GIT
#

tag:
	touch README.rst
	git tag $(VERSION)
	git commit -a -m "$(VERSION)"
	git push
