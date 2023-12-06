from demo37module import *
#independent function
#decorator method
@div_decorator
def division(a,b):
	print(f'res of {a} by {b} is {a/b}')
if __name__ == '__main__':
	num1=int(input('Enter num1:'))
	num2=int(input('Enter num2:'))
	division(num1,num2)