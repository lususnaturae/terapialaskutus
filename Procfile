web: gunicorn config.wsgi:application
worker: celery worker --app=therapyinvoicing.taskapp --loglevel=info
