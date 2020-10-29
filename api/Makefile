virtualenv:
	virtualenv -p python3 env

deps-pre:
	pip install pip-tools

deps-compile:
	pip-compile requirements.in -o requirements.txt

deps-upgrade: deps-pre
	pip-compile requirements.in -o requirements.txt --upgrade

deps-install:
	pip-sync requirements.txt

deps: deps-pre deps-install

server: server-dev

server-dev:
	python drf_facebook_auth_api/manage.py runserver localhost:8000

migrate:
	drf_facebook_auth_api/manage.py migrate

migrations:
	drf_facebook_auth_api/manage.py makemigrations

user:
	drf_facebook_auth_api/manage.py createsuperuser

seed:
	drf_facebook_auth_api/manage.py seed --reset-db --admin

db: migrate seed