# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.12.3
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

WORKDIR .

COPY requirements.txt .

RUN apt-get update && apt-get -y install libpq-dev gcc

RUN python -m venv env && .\env\Scripts\activate

RUN python -m pip install -r requirements.txt

COPY . .

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD python manage.py collectstatic && python manage.py migrate && python manage.py admin_create && gunicorn 'tasks.wsgi' --bind=0.0.0.0:8000
