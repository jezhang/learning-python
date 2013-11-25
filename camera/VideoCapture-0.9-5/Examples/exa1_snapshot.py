from VideoCapture import Device
from functions import sid

cam = Device()
cam.saveSnapshot('photos\photo%s.jpg' %sid(), timestamp=3, boldfont=1)
