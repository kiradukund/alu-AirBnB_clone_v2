#!/usr/bin/env bash
# Sets up web servers for deployment of web_static
apt-get -y update
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

echo "<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>" > /data/web_static/releases/test/index.html

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

cat > /etc/nginx/sites-available/default << 'NGINX'
server {
listen 80 default_server;
listen [::]:80 default_server;
server_name _;
root /var/www/html;
index index.html index.htm;
location /hbnb_static/ {
alias /data/web_static/current/;
index index.html;
}
location / {
try_files $uri $uri/ =404;
}
}
NGINX

ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
nginx -s stop 2>/dev/null; sleep 1; service nginx start
exit 0
