FROM python:3-slim

WORKDIR /app

COPY requirements.txt /app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

EXPOSE 5021

ENV FLASK_APP=app.py

CMD ["gunicorn", "app:app", "--bind=0.0.0.0:5021", "--workers=5", "--access-logfile=/app/access.log", "--error-logfile=/app/error.log"]


# docker build -t onam-card-gen .
# docker run -d -p 5021:5021 onam-card-gen

