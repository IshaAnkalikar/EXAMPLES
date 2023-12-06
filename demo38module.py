#decorator function 
#inner function
def decorator(w):
	def inner(name):
		if name=="mahi":
			print(f' Hello {name} access granted..!')
		else:
			w(name)
	return inner
	