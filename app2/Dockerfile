
FROM python:3.9-slim-buster

WORKDIR /app

ADD . /app

RUN pip install --no-cache-dir flask

EXPOSE 1717

CMD ["python", "app.py"]
