#!/bin/bash

# Install Nginx
apt-get update
apt-get install -y nginx

# Configure the redirection in Nginx
echo '
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    # Other location blocks...
}
' > /etc/nginx/sites-available/default

# Enable the configuration
ln -s /etc/nginx/sites-available/default /etc/nginx/sites-enabled/

# Restart Nginx to apply the changes
service nginx restart

