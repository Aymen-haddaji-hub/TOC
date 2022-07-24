#!/bin/sh
gunicorn  --chdir api TOC_API:app -w 2 --threads 2 -b 127.0.0.1:5000
