
'''
how to use else in loop
'''

def isPrime(y):
	x = y // 2
	while x > 1 :
		if y % x == 0:
			print('%d has factor %d' % (y,x))
			break
		x -= 1
	else:
		print ('%d is prime' % y)

def test_else():
	i = 0
	while i < 10:
		i += 1
		break
	else:
		print 'else branch when i = %d' % i

def main():
	test_else()
	for i in range(100):
		isPrime(i)

if __name__ == '__main__':
	main()