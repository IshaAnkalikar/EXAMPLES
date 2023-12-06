#Exception Object Propagation
def alpha():
	try:
		print('Conn 4 estd')
		num1=int(input('Enter num1:'))
		num2=int(input('Enter num2:'))
		res=num1/num2
		print(f'res is {res}')
	except Exception as e:
		print('Exception handled successfully!')
		print(f'The exception info is {e.args}')
		print('Conn 4 Terminated')
def beta():
	print('Conn 3 estd')
	alpha()
	print('Conn 3 Terminated')
def gamma():
	print('Conn 2 estd')
	beta()
	print('Conn 2 Terminated')
if __name__ == '__main__':
	print('Conn 1 estd')
	gamma()
	print('Conn 1 Terminated')