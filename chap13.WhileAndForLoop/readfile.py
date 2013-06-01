
def func1():
	f = open('readfile.py')
	while True:
		char = f.read(1)
		if not char: break
		print(char)

def func2():
	for char in open('readfile.py').read():
		print(char)

def main():
	func1()

if __name__ == '__main__':
	main()