import os

import paho.mqtt.client as mqtt
from datetime import datetime

def on_connect_webserver(client, userdata, flags, rc):
    print(f"websever connected with result code {rc}")
    client.subscribe("photo")

def on_message_webserver(client, userdata, message):
    if message.topic == "photo":
        photo = message.payload
        name = datetime.now().strftime("%d-%m-%Y %H.%M.%S") + ".png"
        path = os.path.join("../flaskapp/static", "img", name)
        f = open(path, "wb")
        f.write(photo)
        print("Image Received")
        f.close()

webserver = mqtt.Client()
webserver.on_connect = on_connect_webserver
webserver.on_message= on_message_webserver
webserver.username_pw_set("webserver","webserver")
webserver.connect("localhost", 1883, 200)
webserver.loop_forever()