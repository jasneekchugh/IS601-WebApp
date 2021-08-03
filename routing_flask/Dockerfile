
FROM python:3.8

EXPOSE 5003

WORKDIR /routing_flask

COPY requirements.txt /routing_flask
RUN pip install  -r requirements.txt --upgrade pip

COPY . /routing_flask

CMD python app.py