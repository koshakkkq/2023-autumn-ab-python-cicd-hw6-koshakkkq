# Use an official Python runtime as a parent image
FROM python:3.10 AS builder

# Set work directory
WORKDIR /opt/build

# Install Poetry
RUN pip install poetry

# Copy only requirements to cache them in docker layer
COPY pyproject.toml poetry.lock README.md src config ./

# Project initialization:
RUN poetry config virtualenvs.create false \
    && poetry install --no-dev

# Start final image
FROM python:3.10-slim

EXPOSE 8000

WORKDIR /opt/app

# Copy only the relevant files from the builder
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin
COPY ./ /opt/app/

# Application entrypoint
CMD ["uvicorn", "homework_app.main:app", "--host", "0.0.0.0", "--port", "8000", "--app-dir", "src"]