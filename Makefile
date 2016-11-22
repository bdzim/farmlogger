build_docker:
	docker-compose -f dev.yml build

run_docker: build_docker
	docker-compose -f dev.yml up
	docker-compose -f dev.yml run django python manage.py migrate

manage_docker: MANAGE = ${MANAGE}
manage_docker:
	docker-compose -f dev.yml run django python manage.py ${MANAGE}

migrate:
	docker-compose -f dev.yml run django python manage.py makemigrations
	docker-compose -f dev.yml run django python manage.py migrate

pytest: 
	docker-compose -f dev.yml run django py.test

flake8: 
	docker-compose -f dev.yml run --rm django bash -c "flake8"

coverage: 
	docker-compose -f dev.yml run django coverage run manage.py test
	docker-compose -f dev.yml run django coverage html
