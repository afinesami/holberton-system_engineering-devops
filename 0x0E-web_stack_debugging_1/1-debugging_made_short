#!/usr/bin/env bash
# script to listen the port 80
sudo sed -i 's/8080/80/g' /etc/nginx/sites-enabled/default /etc/nginx/sites-available/default
sudo service nginx restart
sudo pkill -o nginx