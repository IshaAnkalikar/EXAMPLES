# use of raise keyword in python
def odd_even(n):
	if n%2==0:
		raise ValueError('The number is already even')
	else:
		print('The number is odd')
if __name__ == '__main__':
	data=int(input('enter a number:'))
	odd_even(n=data)