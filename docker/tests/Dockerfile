FROM python:3.10-slim

EXPOSE 8000

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

WORKDIR /opt/app

COPY poetry.lock .
COPY pyproject.toml .
COPY README.md .
COPY /src/ ./src/
COPY /tests ./tests/

RUN pip install poetry
RUN poetry install

CMD ["poetry", "run", "uvicorn", "--app-dir=src" ,"--host=0.0.0.0","--port=8000","homework_app.main:app", "--reload"]
