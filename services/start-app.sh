#!/bin/bash
 
echo "stop existing gunicorn"
pkill -f "gunicorn"

echo "Reloading systemd..."
sudo systemctl daemon-reload
 
echo "Enabling django-app service..."
sudo systemctl enable run-docs-parser-api
 
echo "Starting django-app service..."
sudo systemctl start run-docs-parser-api
 
echo "Fetching logs for docs_parser_api..."
sudo journalctl -fu run-docs-parser-api
