
mkdir -p /var/run/sshd /var/www/app/web
echo > /etc/motd
echo 'export PS1="\[\033[01;32m\]\u@\h\[\033[00m\]:\[\033[01;34m\]\w\[\033[00m\]\$ "' > /root/.bashrc
echo 'alias start="supervisorctl start"' >> /root/.bashrc
echo 'alias restart="supervisorctl restart"' >> /root/.bashrc
echo 'alias stop="supervisorctl stop"' >> /root/.bashrc
echo 'alias status="supervisorctl status"' >> /root/.bashrc
echo 'source /var/www/env/bin/activate' >> /root/.bashrc
echo 'cd /var/www/app' >> /root/.bashrc

echo 'export DJANGO_SETTINGS_MODULE=app.settings_prod' >> /root/.bashrc

sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config

mkdir /root/.ssh

mkdir -p /var/www/app/log
mkdir -p /var/run/mysqld
chown mysql /var/run/mysqld


