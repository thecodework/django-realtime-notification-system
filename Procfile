release: python manage.py migrate
web: daphne notification_projects.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A notification_projects worker --pool=solo -l info
celerybeat: celery -A notification_projects beat -l info