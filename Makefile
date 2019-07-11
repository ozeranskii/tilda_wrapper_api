# This file is part of tilda_wrapper_api.
# https://github.com/ozeranskiy/tilda_wrapper_api

# Licensed under the MIT license:
# http://www.opensource.org/licenses/MIT-license
# Copyright (c) 2019, Sergey Ozeranskiy <sergey.ozeranskiy@gmail.com>

.PHONY: docs

# lists all available targets
list:
	@sh -c "$(MAKE) -p no_targets__ | awk -F':' '/^[a-zA-Z0-9][^\$$#\/\\t=]*:([^=]|$$)/ {split(\$$1,A,/ /);for(i in A)print A[i]}' | grep -v '__\$$' | grep -v 'make\[1\]' | grep -v 'Makefile' | sort"
# required for list
no_targets__:

# install all dependencies (do not forget to create a virtualenv first)
init:
	pip install pipenv --upgrade
	pipenv install --dev

# test your application (tests in the tests/ directory)
test: unit

unit:
	@coverage run --branch `which nosetests` -vv -s tests/
	@coverage report -m

# show coverage in html format
coverage-html: unit
	@coverage html

# run tests against all supported python versions
tox:
	@tox

# build docs
docs:
	cd docs && make html
	@echo "\033[95m\n\nBuild successful! View the docs homepage at docs/_build/html/index.html.\n\033[0m"
