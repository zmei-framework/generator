[uwsgi]
socket = 0.0.0.0:8000

# Django-related settings
# the base directory (full path)
chdir           = /var/www/app
# Django's wsgi file
module          = app.wsgi
# the virtualenv (full path)
;home            = /var/www/env

# process-related settings
# master
master          = true
# maximum number of worker processes
processes       = 2
# the socket (use the full path to be safe
#socket          = /path/to/your/project/mysite.sock
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum          = true
