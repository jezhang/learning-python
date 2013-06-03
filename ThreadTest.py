import threading
import datetime

class HelloWorldThread(threading.Thread):
	def run(self):
		now = datetime.datetime.now()
		print '%s.says Hello World at time: %s' % (self.getName(), now)

def main():
	for i in range(4):
		t = HelloWorldThread()
		t.start()

if __name__ == '__main__':
	main()