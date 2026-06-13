@echo off
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout server-key.key -out server-cert.crt -config server-cert.cnf
echo Certificate and key generated successfully.
pause
