#Method Overloading
#Example-1
class Calc:
	def add(self,a):
		return a+10
	def add(self,a,b):
		return a+b
	def add(self,a,b,c):
		return a+b+c
if __name__ == '__main__':
	c=Calc()
	c.add(a=10)
