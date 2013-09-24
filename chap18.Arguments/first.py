def f(a):
	# a[0] = 99
	a = 'spam'

b = [0,88]
f(b)
print(b)


def changer(a,b):
	a = 2
	b[0] = 'spam'

X = 1
L = [1,2]
changer(X, L)
print(X,L)