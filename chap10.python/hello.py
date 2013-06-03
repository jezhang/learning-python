def abc():
	a,b = 1,2
	if a < b:
		c = 3
	return c

def reply():
	while True:
		reply = raw_input('>>>')
		if reply == 'stop' : break
		print(reply.upper())

def main():
	reply()


if __name__ == '__main__':
	main()