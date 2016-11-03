=============================
{{cookiecutter.project_name}}
=============================

.. contents::


{{cookiecutter.project_short_description}}


Quickstart
----------

A Makefile is provided with common tasks::

    $ make help

    clean - remove build artifacts and python artifacts
    .env - make a virtual environment
    lint - check style with flake8
    isort - check import order with isort
    freeze-requirements - freeze the requirements with pip-compile
    test - run tox



Dependency Workflow
-------------------

This project uses `pip-tools`_ to manage dependencies.

In short, ``requirements.in``

* Unpinned or SemVer ranges
* Not passed to pip

Are compiled to ``requirements.txt``

* Pinned dependencies
* Define the build

.. _`pip-tools`: https://github.com/nvie/pip-tools
