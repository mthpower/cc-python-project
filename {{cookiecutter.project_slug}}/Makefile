.PHONY: help clean build lint isort test freeze-requirements docker-build docker-run

bin = .env/bin
pip = $(bin)/pip
tox = $(bin)/tox
pip-compile = $(bin)/pip-compile
flit=$(bin)/flit

help:
	@echo "clean - remove build artifacts and python artifacts"
	@echo ".env - make a virtual environment"
	@echo "lint - check style with flake8"
	@echo "isort - check import order with isort"
	@echo "freeze-requirements - freeze the requirements with pip-compile"
	@echo "test - run tox"
	@echo "docker-build - build a docker container"
	@echo "docker-run - run the built docker container in the foreground"


.env:
	python3 -m venv .env --clear
	$(pip) install --upgrade pip
	$(pip) install --upgrade wheel tox pip-tools flit

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -name '__pycache__' -type d -exec rm -rf {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +

build: .env clean
	FLIT_NO_NETWORK=True $(flit) wheel

lint: .env
	$(tox) -e lint

isort: .env
	$(tox) -e isort

test: .env
	$(tox)

freeze-requirements: .env
	$(pip-compile) requirements.in
	$(pip-compile) test_requirements.in

docker-build: build
	docker build . -t {{cookiecutter.project_slug}}

docker-run: docker-build
	docker run -it {{cookiecutter.project_slug}}
