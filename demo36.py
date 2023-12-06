'''
Write a nested function prgm for the given independent 
function
#independent function
def wish(name):
	print(f' Hello {name} access not granted..!')
'''

def decorator(w):
	def inner(name):
		if name=="mahi":
			print(f' Hello {name} access granted..!')
		else:
			w(name)
	return inner
#independent function
def wish(name):
	print(f' Hello {name} access not granted..!')
if __name__ == '__main__':
	data=input('Enter a name:')
	res=decorator(w=wish)
	res(name=data)