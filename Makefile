.PHONY: install
install:
	poetry install

.PHONY: format
format:
	poetry run black . --check
	poetry run isort . --profile=black
	poetry run pre-commit run --all-files
