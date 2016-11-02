.PHONY: help clean lint isort test freeze-requirements

bin = .env/bin
pip = $(bin)/pip
tox = $(bin)/tox
pip-compile = $(bin)/pip-compile

help:
	@echo "clean - remove build artifacts and python artifacts"
	@echo ".env - make a virtualenv"
	@echo "lint - check style with flake8"
	@echo "isort - check import order with isort"
	@echo "freeze-requirements - freeze the requirements with pip-compile"
	@echo "test - run tox"

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -name '__pycache__' -type d -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

lint: .env
	$(tox) -e lint

isort: .env
	$(tox) -e isort

test: .env
	$(tox)

freeze-requirements: .env
	$(pip-compile) requirements.in
	$(pip-compile) test_requirements.in

.env:
	rm -rf ./.env/
	virtualenv .env
	$(pip) install --upgrade pip
	$(pip) install --upgrade setuptools wheel
	$(pip) install tox ipdb pip-tools
