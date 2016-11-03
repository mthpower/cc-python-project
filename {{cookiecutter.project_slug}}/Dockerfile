FROM python:3.5-alpine

WORKDIR /usr/src/{{cookiecutter.project_slug}}

COPY requirements.txt .
COPY dist/{{cookiecutter.py_namespace}}*.whl .

RUN pip install --no-cache-dir -U pip
RUN pip install --no-cache-dir --no-deps -r requirements.txt
RUN pip install {{cookiecutter.py_namespace}}*.whl

CMD {{cookiecutter.project_slug}}
