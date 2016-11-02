FROM python:3.5-alpine

RUN mkdir -p /opt/{{cookiecutter.project-slug}}
WORKDIR /opt/{{cookiecutter.project-slug}}

COPY requirements.txt /opt/{{cookiecutter.project-slug}}/
RUN pip install --no-cache-dir --no-deps -r requirements.txt
COPY . /opt/{{cookiecutter.project-slug}}

CMD {{cookiecutter.project_slug}}
