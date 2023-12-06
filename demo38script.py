from demo38module import *
#independent function
#decorator method
@decorator
def wish(name):
	print(f' Hello {name} access not granted..!')
if __name__ == '__main__':
	data=input('Enter a name:')
	wish(name=data)
