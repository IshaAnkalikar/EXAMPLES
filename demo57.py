#Example for cyclic inheritance
class A:
	pass
class B(A):
	def a(self):
		print('b')
class A(B):
	def a(self):
		print('a')
		super(B,self).a()

class B(A):
	def a(self):
		print('b.1')
		super(B,self).a()
if __name__ == '__main__':
	ref=B()
	ref.a()
