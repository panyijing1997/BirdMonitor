import random

from phue import Bridge
import logging
logging.basicConfig()

b = Bridge('192.168.86.39')

#Uncomment this line to register the app (see below)
#b.connect()

#Change the light state

b.set_light(11, 'on', True)
b.set_light(11, 'xy', [0.1656,0.0536])