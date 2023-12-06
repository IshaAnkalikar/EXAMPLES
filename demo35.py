#Example-2-decorators
def div_decorator(d):
	def wrapper(x,y):
		if y==0:
			print('Division is not possible')
		else:
			d(x,y)
	return wrapper
#independent function
def division(a,b):
	print(f'Result of {a} by {b} is {a/b}')
if __name__ == '__main__':
	num1=int(input('Enter num1:\n'))
	num2=int(input('Enter num2:\n'))
	res=div_decorator(d=division)
	res(num1,num2)

	