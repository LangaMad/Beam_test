FROM python:3.11-alpine

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn","core.wsgi.application","--bind","0.0.0.0:8000"]