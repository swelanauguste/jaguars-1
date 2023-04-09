#!/bin/sh

# if [ "$DATABASE" = "postgres" ]
# then
#     echo "Waiting for postgres..."

#     while ! nc -z $SQL_HOST $SQL_PORT; do
#       sleep 0.1
#     done

#     echo "PostgreSQL started"
# fi
# python manage.py flush --noinput
python manage.py migrate

python manage.py makemigrations
python manage.py migrate
# python manage.py createsuperuser --username kingship --email kingship.lc@gmail.com --noinput

# python manage.py add_venues
# python manage.py add_teams
# python manage.py add_dismissal_list
# python manage.py add_south_castries_players
# python manage.py add_jaguars_players

python manage.py collectstatic --noinput

exec "$@"