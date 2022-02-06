# syntax=docker/dockerfile:1
FROM eclipse-mosquitto:2.0.12
WORKDIR /mosquitto
COPY config config
RUN mosquitto_passwd -c -b /mosquitto/config/pwfile webserver webserver
RUN mosquitto_passwd -b /mosquitto/config/pwfile browser browser
RUN mosquitto_passwd -b /mosquitto/config/pwfile camera camera

EXPOSE 1883 8883