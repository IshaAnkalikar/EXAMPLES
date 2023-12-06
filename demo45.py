#Static methods
#Example-1 for static method
class ABCmath:
	#static method-1
	@staticmethod
	def add(x,y):
		return x+y

	#static method-2
	@staticmethod
	def sub(x,y):
		return x-y

	#static method-3
	@staticmethod
	def mul(x,y):
		return x*y

	#static method-4
	@staticmethod
	def div(x,y):
		return x/y 
if __name__ == '__main__':
	x=int(input('enter x value:'))
	y=int(input('enter y value:'))
	a=ABCmath()
	res=a.mul(x=x,y=y)
	print(f'The res is {res} ')