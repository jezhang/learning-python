
def test_for_1():
	for x in ['spam','eggs','ham']:
		print x

def test_for_2():
	sum = 0
	prod = 1
	for x in [1,2,3,4]:
		sum += x
		prod *= x
	print (sum,prod)

def test_for_3():
	S = 'lumberjack'
	T = ("and","I'm","okay")
	for x in S: print(x)

def test_for_4():
	items = ['aaa',111,(4,5),2.01]
	tests = [(4,5),3.14]
	for key in tests:
		for item in items:
			if item == key:
				print(key, "was found")
				break
			else:
				print(key, "not found")

def main():
	# test_for_1()
	# test_for_2()
	# test_for_3()
	# test_for_4()


if __name__ == '__main__':
	main()