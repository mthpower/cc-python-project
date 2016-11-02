FROM python:3.5-alpine

RUN mkdir -p /opt/{{cookiecutter.project_slug}}
WORKDIR /opt/{{cookiecutter.project_slug}}

COPY requirements.txt /opt/{{cookiecutter.project_slug}}/
RUN pip install --no-cache-dir --no-deps -r requirements.txt
COPY . /opt/{{cookiecutter.project_slug}}

CMD {{cookiecutter.project_slug}}
