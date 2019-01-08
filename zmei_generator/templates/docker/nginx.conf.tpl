resolver 127.0.0.11 ipv6=off valid=10s;

server {
	listen 80 default_server;
	listen [::]:80 default_server;

    index index.html index.htm;
	root /var/www/app/web;

	server_name _;

	client_max_body_size 300M;
    keepalive_timeout 70;

    location ~ ^/static/ {
       expires 1M;
       access_log off;
       add_header Cache-Control "public";

       root  /var/www/var/;
    }

    location ~ ^/media/ {
       expires 1M;
       access_log off;
       add_header Cache-Control "public";

       root  /var/www/var/;
    }

    # Media: images, icons, video, audio, HTC
    location ~* \.(?:jpg|jpeg|gif|png|ico|cur|gz|svg|svgz|mp4|ogg|ogv|webm|htc|woff|woff2|eot|ttf)$ {
      expires 1M;
      access_log off;
      add_header Cache-Control "public";
    }

    # CSS and Javascript
    location ~* \.(?:css|js)$ {
      expires 1y;
      access_log off;
      add_header Cache-Control "public";
    }

    location / {
        try_files $uri @django;
    }

    location @django {
        set $backend_servers app;

        include uwsgi_params;
        uwsgi_read_timeout 30;
        uwsgi_pass $backend_servers:8000;
    }

}
