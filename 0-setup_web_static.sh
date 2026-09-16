#!/usr/bin/env bash
# Sets up web servers for deployment of web_static
apt-get install -y nginx

mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/

cat > /data/web_static/releases/test/index.html << 'HTML'
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
HTML

ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/

config="server {\n\tlisten 80 default_server;\n\tlisten [::]:80 default_server;\n\troot /var/www/html;\n\tindex index.html index.htm index.nginx-debian.html;\n\tserver_name _;\n\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n\tlocation / {\n\t\ttry_files \$uri \$uri/ =404;\n\t}\n}"
echo -e "$config" > /etc/nginx/sites-available/default

service nginx restart
exit 0
