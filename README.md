# BirdMonitor

I put bread and corns at my kitchen's window and birds come to eat. When I check the window I can see these foods have been eaten, but I hardly see birds and I don't know when they come. So I made this system based on Raspberry Pi + camera. 

### Functions
When any birds go into camera's view, the deep learning model will detect it then the camera will take a picture and save it so that I can check later (via a simple flask app, running on RPi).

At the same time, it will turn on one of phillip smart lights in my working room and set the light color to purple. So if I am at home, I can go to the kitchen see the bird :)
When birds gone, the light will be turn off.

### Privacy
All programs are running on RPi, everything is in my home network. No cloud service.

### Techs
- Raspberry Pi + Pi Camera Module
- MQTT (using eclipse-mosquitto)
- Python Flask (just to make a simple way to check saved photos)
- TensorFlow Lite for detecting birds
- Phillip Hue REST API 

## Run
### install independencies
```shell
$ pip install -r requirements.txt
```
### build and run the mqtt broker image
In the `mqtt` folder:
```shell
$ docker build -t birdmqtt .
$ docker run -p 1883:1883 birdmqtt
```
### run the component for hardware operating and deep learning
In the `operation` folder:
```shell
$ python3 bird_detection.py
```
if Phillip Hue is unavaible, comment codes for sending request to Hue bridge in `operation/bird_detection.py`.
### run the flask app
In the `flaskapp` folder:
```shell
$ python3 app.py
```
