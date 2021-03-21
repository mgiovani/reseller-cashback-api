install:
	cp env.example .env
	poetry install
	@echo "=================================================================="
	@echo "Now set your envvars at .env file and use source .env to load them"
	@echo "=================================================================="

dev-db:
	poetry run docker-compose -f dev.yml up -d

run:
	poetry run python reseller_cashback_api/manage.py runserver

makemigrations:
	poetry run python reseller_cashback_api/manage.py makemigrations

migrate:
	poetry run python reseller_cashback_api/manage.py migrate

run-docker-mode:
	docker-compose -f docker-compose.yml up

test:
	PYTHONPATH=reseller_cashback_api poetry run pytest

lint:
	poetry run flake8 --format pylint