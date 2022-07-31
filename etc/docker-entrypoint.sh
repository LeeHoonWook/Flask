# !/bin/bash

set -e


flask db upgrade

gunicorn --bind unix:/tmp/gunicorn.sock --workers 2 --threads 8 --reload --access-logfile - 'gogglekaap:create_app()'