FROM python:3.6

WORKDIR /app

COPY requirements.txt /app
RUN pip install -r requirements.txt

COPY . /app

WORKDIR /app
ENV PORT=8080
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 app:app