from flask import Flask, render_template, request, make_response
from flask_mqtt import Mqtt
from datetime import datetime
import sys
import os

app = Flask(__name__)
app.config['MQTT_BROKER_URL'] = "localhost"
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config['MQTT_BROKER_PORT'] = 1883
app.config['MQTT_REFRESH_TIME'] = 1.0  # refresh time in seconds
app.config['MQTT_KEEPALIVE'] = 60
app.config['MQTT_USERNAME'] = 'webserver'
app.config['MQTT_PASSWORD'] = 'webserver'
app.config['MQTT_TLS_ENABLED'] = False
app.config['MQTT_CLEAN_SESSION'] = True
mqtt = Mqtt(app)
mqtt.subscribe('photo')

@mqtt.on_connect()
def handle_connect(client, userdata, flags, rc):
    print("client for server connected", flush=True, file=sys.stderr)

@mqtt.on_topic("photo")
def test1(client, userdata, message):
    photo = message.payload
    name = datetime.now().strftime("%d-%m-%Y %H.%M.%S") + ".png"
    path = os.path.join("static", "img", name)
    f = open(path, "wb")
    f.write(photo)
    print("Image Received")
    f.close()


@app.route("/")
def showfiles():
    path=os.path.join("static", "img")
    filelist=list(os.listdir(path))
    template={
        "filelist":filelist
    }
    return render_template("index.html",**template)

@app.route("/<imageName>")
def image(imageName):
    path = "/static/img/" + str(imageName)
    template={
        "path":path
    }
    return render_template("birdphoto.html",**template)





if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)