#!/usr/bin/env bash
# Configures the web servers for redundancy

# Update package lists
apt update

# Install necessary packages (e.g., Nginx)
apt install -y nginx

# Set up monitoring and health checks
# For simplicity, we'll just ensure Nginx is running

# Ensure that both web servers are serving the same content
# For demonstration purposes, we'll just create a simple HTML file
echo "<html><body><h1>Hello World!</h1></body></html>" > /var/www/html/index.html

# Restart the web server
service nginx restart

