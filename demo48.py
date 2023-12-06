#Hierarchical inheritance(Multi-level + single-level)
#Example-1
class A:
	def disp1(self):
		print('This is from class A')
class B:
	def disp2(self):
		print('This is from class B')
class C(A):
	def disp3(self):
		print('This is from class C')
class D(A):
	def disp4(self):
		print('This is from class D')
class E(C):
	def disp5(self):
		print('This is from class E')
if __name__ == '__main__':
	#multi-level
	ref1=E()
	ref1.disp1()
	ref1.disp3()
	ref1.disp5()

	#single-level
	ref2=D()
	ref2.disp1()

