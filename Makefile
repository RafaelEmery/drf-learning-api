migrate:
	python manage.py migrate

make-migrations:
	python manage.py makemigrations

run:
	python manage.py runserver

create-super-user:
	python manage.py createsuperuser

shell:
	python manage.py shell