debconf-set-selections <<< 'mysql-server mysql-server/root_password password 123123'
debconf-set-selections <<< 'mysql-server mysql-server/root_password_again password 123123'
apt-get update && apt-get install -y supervisor openssh-server nginx vim htop curl net-tools mysql-client redis-server mysql-server rsync

python -m venv /var/env
/var/env/bin/pip install uwsgi

