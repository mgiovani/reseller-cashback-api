install:
	cp env.example .env
	poetry install
	@echo "=================================================================="
	@echo "Now set your envvars at .env file and use source .env to load them"
	@echo "=================================================================="

run:
	poetry run python reseller_cashback_api/manage.py runserver

make-migrations:
	poetry run python reseller_cashback_api/manage.py make-migrations

migrate:
	poetry run python reseller_cashback_api/manage.py migrate

run-docker-mode:
	docker-compose -f docker-compose.yml up

test:
	poetry run python reseller_cashback_api/manage.py test

lint:
	poetry run flake8 --format pylint
