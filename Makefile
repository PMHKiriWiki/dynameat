include ./back/.env
export

export DEBUG =
MANAGE_CMD = python manage.py

SCRIPTS_DIR := scripts
FILL_SCRIPT := $(SCRIPTS_DIR)/fill_database.py

.PHONY: fill_database

fill-database:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} fill_database

up:
	docker compose ${COMPOSE_FILES} up --build -d

down:
	docker compose ${COMPOSE_FILES} down

downup:
	docker compose ${COMPOSE_FILES} down; \
	docker compose ${COMPOSE_FILES} up --build -d

shell:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django bash

logs:
	docker logs -f ${COMPOSE_PROJECT_NAME}_django

frontlogs:
	docker logs -f ${COMPOSE_PROJECT_NAME}_vue

createsuperuser:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} createsuperuser

makemigrations:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} makemigrations

migrate:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} migrate

djangoshell:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} shell

restart-nextjs:
	docker restart -it ${COMPOSE_PROJECT_NAME}_nextjs

restart-django:
	docker restart -it ${COMPOSE_PROJECT_NAME}_nextjs
