#Decorators in python 
#Example-1
#Inner functions and closures
def marriage_agency(h):
	def wrap_lights():
		print('Lights installed..!')
		h()
	return wrap_lights
#independent function
def house():
	print('This is my house')
if __name__ == '__main__':
	res=marriage_agency(h=house)
	res()