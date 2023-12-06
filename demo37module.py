#decorator function
def div_decorator(d):
	def wrapper(x,y):
		if y==0:
			print('Division is not possible')
		else:
			d(x,y)
	return wrapper