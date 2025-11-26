FROM python:3.8

RUN pip install flask

COPY . /app
WORKDIR /app

USER root

EXPOSE 5000

COPY /tmp /tmp

CMD ["python", "main.py"]
