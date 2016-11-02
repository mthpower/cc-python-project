.PHONY: help clean lint isort test freeze-requirements

help:
	@echo "clean - remove build artifacts and python artifacts"
	@echo ".env - make a virtualenv and activate it"
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
	tox -e lint

isort: .env
	tox -e isort

test: .env
	tox

requirements.txt: .env requirements.in
	pip-compile requirements.in

test_requirements.txt: .env requirements.txt test_requirements.in
	pip-compile test_requirements.in

freeze-requirements: .env *requirements.txt

.env:
	rm -rf ./.env/
	virtualenv .env
	./.env/bin/pip install --upgrade pip
	./.env/bin/pip install --upgrade setuptools wheel
	./.env/bin/pip install tox ipdb pip-tools
	. ./.env/bin/activate
