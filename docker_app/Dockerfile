FROM python:3.6

# add mysql config before installation, so it is initialised properly
RUN mkdir -p /etc/mysql
COPY my.conf /etc/mysql/my.cnf

ADD install.sh .
RUN bash install.sh

ADD configure.sh .
RUN bash configure.sh

EXPOSE 80
EXPOSE 22

ENV DJANGO_SETTINGS_MODULE "app.settings_prod"

COPY nginx.conf /etc/nginx/sites-enabled/default
COPY redis.conf /etc/redis/redis.conf
COPY uwsgi.ini /etc/uwsgi.ini

COPY sv/*.conf /etc/supervisor/conf.d/
COPY deploy.sh /var/www/
RUN chmod +x /var/www/deploy.sh

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]