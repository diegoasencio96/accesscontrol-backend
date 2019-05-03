#!/bin/bash


#rm -rf apps/*/migrations/0*.py
#rm -rf apps/*/migrations/0*.pyc
python /srv/accesscontrol-backend/src/accesscontrol/manage.py makemigrations
python /srv/accesscontrol-backend/src/accesscontrol/manage.py migrate                  # Apply database migrations
python /srv/accesscontrol-backend/src/accesscontrol/manage.py collectstatic --noinput  # Collect static files
# Prepare log files and start outputting logs to stdout
touch /srv/accesscontrol-backend/src/accesscontrol/logs/gunicorn.log
touch /srv/accesscontrol-backend/src/accesscontrol/logs/access.log
tail -n 0 -f /srv/accesscontrol-backend/src/accesscontrol/logs/*.log &

# Start Gunicorn processes
echo Starting Gunicorn.


exec gunicorn accesscontrol.wsgi:application \
    --name PARQUESOFT-META \
    --bind 0.0.0.0:8000 \
    --workers 3 \
    --timeout 3600 \
    --log-level=info \
    --log-file=/srv/accesscontrol-backend/src/accesscontrol/logs/gunicorn.log \
    --access-logfile=/srv/accesscontrol-backend/src/accesscontrol/logs/access.log \
    "$@"

#celery -A sitcol worker -l info
