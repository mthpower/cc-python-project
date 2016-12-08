FROM python:3.5-alpine

WORKDIR /usr/src/{{cookiecutter.project_slug}}

COPY . /usr/src/{{cookiecutter.project_slug}}

RUN pip install --no-cache-dir -U pip \
    && pip install wheel \
    && python setup.py bdist_wheel \
    && pip install --no-cache-dir --no-deps -r requirements.txt \
    && pip install dist/{{ cookiecutter.project_slug.lower().replace('-', '_') }}*.whl

RUN rm -rf /usr/src/{{cookiecutter.project_slug}}

CMD [ "{{cookiecutter.project_slug}}" ]
