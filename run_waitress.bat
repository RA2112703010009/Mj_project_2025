@echo off
waitress-serve --listen=0.0.0.0:443 app:app --certfile=certs/cert.pem --keyfile=certs/key.pem
pause
