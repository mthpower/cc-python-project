=============================
{{cookiecutter.project_name}}
=============================

.. contents::


{{cookiecutter.project_short_description}}


Quickstart
----------

A Makefile is provided with common tasks.


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
