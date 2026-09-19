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

nginx_conf="server {
\tlisten 80 default_server;
\tlisten [::]:80 default_server;
\tserver_name _;
\troot /var/www/html;
\tindex index.html index.htm;
\tlocation /hbnb_static/ {
\t\talias /data/web_static/current/;
\t}
\tlocation / {
\t\ttry_files \$uri \$uri/ =404;
\t}
}"
echo -e "$nginx_conf" | sudo tee /etc/nginx/sites-available/default
sudo ln -sf /etc/nginx/sites-available/default /etc/nginx/sites-enabled/default
sudo nginx -t && sudo service nginx restart
exit 0
