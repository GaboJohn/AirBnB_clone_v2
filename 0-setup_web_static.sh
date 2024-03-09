#!/bin/env bash

# Install Nginx if not already installed
sudo apt-get update
sudo apt-get -y install nginx

# Create necessary folders
sudo mkdir -p /data/web_static/releases/test
sudo mkdir -p /data/web_static/shared
sudo touch /data/web_static/releases/test/index.html

# Create symbolic link
sudo ln -sf /data/web_static/releases/test /data/web_static/current

# Give ownership to the ubuntu user and group
sudo chown -R ubuntu:ubuntu /data/

# Update Nginx configuration
nginx_config="/etc/nginx/sites-available/default"
echo "server {
    location /hbnb_static {
        alias /data/web_static/current;
    }
}" | sudo tee -a $nginx_config

# Restart Nginx
sudo service nginx restart

# Exit successfully
exit 0
