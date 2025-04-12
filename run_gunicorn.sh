#!/bin/bash
gunicorn app:app \
  --bind 0.0.0.0:443 \
  --certfile=certs/cert.pem \
  --keyfile=certs/key.pem
