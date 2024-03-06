include ./back/.env
export

export DEBUG =
MANAGE_CMD = python manage.py

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

createsuperuser:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} createsuperuser

makemigrations:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} makemigrations

migrate:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} migrate

djangoshell:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} shell

restart-django:
	docker restart -it ${COMPOSE_PROJECT_NAME}_django

run-tests:
	docker exec -it ${COMPOSE_PROJECT_NAME}_django ${MANAGE_CMD} test