web: gunicorn nailsalon.wsgi --log-file -
eb: python nailsalon/manage.py collectstatic --noinput; bin/gunicorn_django --workers=4 --bind=0.0.0.0:$PORT nailsalon/settings.py 
