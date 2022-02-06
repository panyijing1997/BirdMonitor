import os
from datetime import datetime
import paho.mqtt.client as mqtt
import numpy as np
import sys
import cv2
from object_detector import ObjectDetector
from object_detector import ObjectDetectorOptions



def on_connect_camera_client(client, userdata, flags, rc):
    print(f"camera connected with result code {rc}")

camera_client = mqtt.Client()
camera_client.on_connect = on_connect_camera_client
#camera_client.on_message= on_message_camera_client
camera_client.username_pw_set("camera","camera")
camera_client.connect("localhost", 1883, 200)
camera_client.loop_start()


camera_id=0
width=640
height=480
num_threads=4
enable_edgetpu=False
model='model3.tflite'
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)


options = ObjectDetectorOptions(
    num_threads=num_threads,
    score_threshold=0.5,
    max_results=10,
    label_allow_list=["bird"],
    enable_edgetpu=enable_edgetpu)
detector = ObjectDetector(model_path=model, options=options)


bird_number=0
camera_ready=True

while True:
    success, image = cap.read()
    if not success:
        sys.exit(
            'ERROR: Unable to read from webcam. Please verify your webcam settings.'
        )
    image = cv2.flip(image, 1)
    # Run object detection estimation using the model.
    detections = detector.detect(image)
    print(len(detections))
    if camera_ready==True and len(detections)!=0:
        name= datetime.now().strftime("%Y-%m-%d %H.%M.%S") + ".png"

        print(name)
        cv2.imwrite(name, image)
        camera_ready=False

        f = open(name, "rb")
        filecontent = f.read()
        byteArr = bytearray(filecontent)
        f.close()
        camera_client.publish("photo", byteArr)
        os.remove(name)

    if len(detections)!=bird_number:
        camera_ready=True

    bird_number= len(detections)
    print(camera_ready)
    # only when detected number changes, let the camera be ready, to avoid the
    # camera keeping taking photos when there's birds.
    # TODO: turn on the light

