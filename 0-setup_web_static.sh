#!/usr/bin/env bash
# Sets up web servers for deployment of web_static
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

printf "server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\tserver_name _;\n\troot /var/www/html;\n\tindex index.html index.htm;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n}\n" > /etc/nginx/sites-available/default

service nginx restart
exit 0
