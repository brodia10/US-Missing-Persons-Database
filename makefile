# Django
SETTINGS_MODULE = local

serve:
	python manage.py runserver --SETTINGS_MODULE=${SETTINGS_MODULE}

migrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

collect:
	python manage.py collectstatic --noinput

super:
	python manage.py createsuperuser

# pip

install:
	pip3 install -r requirements.txt

freeze:
	pip3 freeze > requirements.txt

# virtual env

newenv:
	virtualenv myenv -p python3

startenv:
	source myenv/bin/activate

stopenv:
	deactivate

# Code Formatting - Black
# Black configuration is in pyproject.toml
format:
	black . --config pyproject.toml -v

# Linting - Flake8
# Flake8 configuration is in tox.ini
lint:
	flake8 .

remove_unused:
	autoflake --remove-all-unused-imports --remove-unused-variables -r -i ./*/*