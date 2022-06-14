FROM python:alpine

WORKDIR /app

COPY ./app /app

RUN pip install Flask
RUN pip install -U flask-cors
RUN pip install pymongo

CMD ["python", "index.py"]