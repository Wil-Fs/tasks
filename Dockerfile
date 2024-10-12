ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim as base

WORKDIR .

COPY requirements.txt .

RUN apt-get update && apt-get -y install libpq-dev gcc

RUN python -m pip install -r requirements.txt

COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD python manage.py collectstatic && python manage.py migrate && python manage.py admin_create && gunicorn 'tasks.wsgi' --bind=0.0.0.0:8000
