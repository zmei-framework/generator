debconf-set-selections <<< 'mysql-server mysql-server/root_password password 123123'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 123123'
apt-get update && apt-get install -y supervisor openssh-server nginx vim htop curl net-tools redis-server mariadb-server rsync locales

python -m venv /var/www/env
/var/www/env/bin/pip install --upgrade pip
/var/www/env/bin/pip install uwsgi

locale-gen en_US.UTF-8
localedef -i en_US -f UTF-8 en_US.UTF-8
