.PHONY: clean

help:
	@echo "clean - remove build artifacts and python artifacts"
	@echo "env - make a virtualenv and activate it"
	@echo "lint - check style with flake8"
	@echo "test - run tox"

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

lint: .env
	tox -e lint
	# sh -c ". ./.env/bin/activate; flake8 --exclude=.tox,.env"

test: .env
	# sh -c ". ./.env/bin/activate; tox --skip-missing-interpreters"

.env:
	rm -rf ./.env/
	virtualenv .env
	./.env/bin/pip install --upgrade pip
	./.env/bin/pip install --upgrade setuptools wheel
	./.env/bin/pip install tox ipdb
	. ./.env/bin/activate
