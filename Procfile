release: python manage.py migrate
web: gunicorn storefornt.wegi OR waitress-serve --listen=*:8000 storefreont.wsgi:application
worker: celery -A storefront worker
