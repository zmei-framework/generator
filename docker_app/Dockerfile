FROM python:3.6

ADD install.sh .
RUN bash install.sh
RUN mkdir /var/run/sshd

RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config

RUN mkdir /root/.ssh

RUN mkdir -p /var/log/supervisor

EXPOSE 80
EXPOSE 22

RUN echo 'root:mysuperapp' |chpasswd
COPY sv_nginx.conf /etc/supervisor/conf.d/nginx.conf
COPY nginx.conf /etc/nginx/sites-enabled/default
COPY my.conf /etc/my.conf
COPY redis.conf /etc/redis.conf
COPY sv_sshd.conf /etc/supervisor/conf.d/ssh.conf
COPY uwsgi.ini /etc/uwsgi.ini

CMD ["/usr/bin/supervisord", "-n", "-c", "/etc/supervisor/supervisord.conf"]