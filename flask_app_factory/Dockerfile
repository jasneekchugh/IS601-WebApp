
FROM python:3.8

EXPOSE 5005

WORKDIR /flask_app_factory

COPY requirements.txt /flask_app_factory
RUN pip install  -r requirements.txt --upgrade pip

COPY . /flask_app_factory

CMD python app.py