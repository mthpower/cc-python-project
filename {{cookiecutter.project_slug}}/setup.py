import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='{{cookiecutter.project_slug}}',
    version='{{cookiecutter.version}}',
    packages=('{{cookiecutter.py_namespace}}',),
    description='{{cookiecutter.project_short_description}}',
    long_description=README,
    author='{{cookiecutter.full_name}}',
    author_email='{{cookiecutter.email}}',
    zip_safe=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    entry_points={
        'console_scripts': [
            '{{cookiecutter.project_slug}} = {{cookiecutter.py_namespace}}.{{cookiecutter.py_namespace}}:main',
        ],
    },
)
