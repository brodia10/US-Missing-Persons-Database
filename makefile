# Django
SETTINGS_MODULE = local

serve: startdeps
	python manage.py runserver --settings=config.settings.${SETTINGS_MODULE}

migrations:
	python manage.py makemigrations

showmigrations:
	python manage.py showmigrations

migrate:
	python manage.py migrate

collect:
	python manage.py collectstatic --noinput

super:
	python manage.py createsuperuser

# requirements

install:
	pip install -r requirements.min.txt

freeze: install
	pip freeze > requirements.txt

# virtual env

newenv:
	python3 -m venv venv

startenv:
	source venv/bin/activate

stopenv:
	deactivate

# Tests
# Test True
test:
	python manage.py test --settings=config.settings.test

# Code Formatting - Black
# Black configuration is in pyproject.toml
format:
	black . --config pyproject.toml

# Linting - Flake8
# Flake8 configuration is in tox.ini
lint:
	flake8 .

remove_unused:
	autoflake --remove-all-unused-imports --remove-unused-variables -r -i ./*/*

# Infrastrucutre

startdeps:
	docker-compose up -d

stopdeps:
	docker-compose down

# Installing gis system requirements

ifeq ($(OS),Windows_NT)
    detected_OS := Windows
else
    detected_OS := $(shell sh -c 'uname 2>/dev/null || echo Unknown')
endif

install-gis:
	@sh install_system_deps.sh $(detected_OS)

load-world-boarders:
	python manage.py load_world_boarders


