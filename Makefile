build_docker:
	docker-compose -f dev.yml build

run_docker: build_docker
	docker-compose -f dev.yml up

manage_docker: MANAGE = ${MANAGE}
manage_docker:
	docker-compose -f dev.yml run django python manage.py ${MANAGE}

migrate:
	docker-compose -f dev.yml run django python manage.py makemigrations
	docker-compose -f dev.yml run django python manage.py migrate
