
class Worker:
	def __init__(self,name,pay):
		self.name = name
		self.pay = pay
	def lastName(self):
		return self.name.split()[-1]
	def giveRaise(self,percent):
		self.pay *= (1.0 + percent)

def main():
	bob = Worker("Bob Smith", 50000)
	sue = Worker("Sue Jones",60000)
	print(bob.name)
	print(bob.lastName())
	print(sue.lastName())
	sue.giveRaise(0.1)
	print(sue.pay)

if __name__ == '__main__':
	main()