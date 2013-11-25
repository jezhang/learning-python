from VideoCapture import Device
import time,datetime

interval = 60


def current_datetime_str():
	return datetime.datetime.now().strftime('%Y%m%d%H%M%S')

def main():
	cam = Device(devnum=0)
	print "press 'ctrl + c' to terminate"	
	i = 0
	quant = interval * .1
	starttime = time.time()
	while 1:
	    lasttime = now = int((time.time() - starttime) / interval)
	    vs = current_datetime_str()
	    print i,'|',vs
	    cam.saveSnapshot('photos/ssc%s.jpg' %vs, timestamp=3, boldfont=1)
	    i += 1
	    while now == lasttime:
	        now = int((time.time() - starttime) / interval)
	        time.sleep(quant)

if __name__ == '__main__':
		main()	





