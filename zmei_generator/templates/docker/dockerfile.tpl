FROM python:3.6 as app

RUN apt-get update && apt-get install -y wait-for-it mysql-client && apt-get clean
ENV PYTHONUNBUFFERED 1


RUN mkdir -p /var/www/app/var/media
RUN mkdir -p /var/www/app/web
WORKDIR /var/www/app

COPY *requirements*.txt /var/www/app/

RUN pip install -r requirements.prod.txt

COPY . /var/www/app


ENV DJANGO_SETTINGS_MODULE=app.settings_prod
RUN python manage.py collectstatic --noinput

RUN chmod +x ./deploy/init.sh

VOLUME /var/www/var/media

CMD wait-for-it mysql:3306 -- ./deploy/init.sh


FROM nginx as nginx

RUN apt-get update && apt-get install wait-for-it && apt-get clean

COPY --from=app /var/www/var/static /var/www/var/static
COPY --from=app /var/www/app/web /var/www/app/web
COPY ./deploy/nginx.conf /etc/nginx/conf.d/default.conf

VOLUME /var/www/var/media

CMD nginx -g 'daemon off;'