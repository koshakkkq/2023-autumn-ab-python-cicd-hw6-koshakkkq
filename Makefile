lint:
	poetry run black src tests
	poetry run flake8 src tests
	poetry run pylint src
	poetry run mypy src/homework_app tests
test:
	poetry run pytest tests
install:
	poetry install