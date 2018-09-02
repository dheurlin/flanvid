#! /bin/bash
python manage.py migrate
python manage.py collectstatic
python ./manage.py shell -c "from django.contrib.auth.models import User; User.objects.create_superuser('dhack', 'admin@example.com', 'hackehackspett')"

uwsgi --ini uwsgi.ini

