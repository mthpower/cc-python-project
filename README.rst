===========================
CC Python Project
===========================

.. contents::

A cookiecutter for a Python Project. Contains my personal preferences and opinions.

Features
--------

* Testing with ``pytest``
* Reproducable testing with ``tox``
* Easy building of wheels with ``flit``
* Requirements freezing workflow with ``pip-tools``
* Python 3 only
* Makefile for common development tasks
* Dockerfile

N.B.: This is aimed at being a starting point for a Python project, not a python library.

Quickstart
----------

Prerequisites:

* Python > 3.4
* Docker

Install cookiecutter:

``$ pip install cookiecutter``

Scaffold a project:

``$ cookiecutter gh:mthpower/cc-python-project``

And follow the prompts.
