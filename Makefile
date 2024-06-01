lint-fix:
	poetry run black .
	poetry run isort .
	poetry run flake8 .
.PHONY: lint-fix

test:
	poetry run pytest --cov=dojo tests/
.PHONY: test