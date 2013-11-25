from VideoCapture import Device
from functions import sid

## use the first video-device which is found
## devnum=1 uses the second one and so on
cam = Device(devnum=0)

## a bold fontstyle is also available
cam.saveSnapshot('photos/ssc%s.jpg' %sid(), timestamp=3, boldfont=1)


