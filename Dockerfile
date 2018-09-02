FROM python:3.6
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src
ADD ./flanvid /src
ADD ./requirements requirements
ADD ./startup.sh startup.sh
ADD ./uwsgi.ini uwsgi.ini
RUN pip install -r requirements

CMD ./startup.sh flanvid 5
#RUN python manage.py migrate
#RUN python manage.py collectstatic
