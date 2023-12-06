class calc:
	def add(self,a=None,b=None,c=None):
		if a!=None and b!=None and c!=None:
			return a+b+c
		elif  a!=None and b!=None:
			return a+b
		elif  a!=None:
			return a+10
		else:
			print('Enter atleast one value')
if __name__ == '__main__':
	c=calc()
	print(c.add(a=10,b=20,c=30))