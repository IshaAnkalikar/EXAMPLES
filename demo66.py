#inner classes Example-1
class outer:
	def __init__(self):
		print('outer class constructor')
	class inner:
		def __init__(self):
			print('inner class constructor')
		def disp(self):
			print('Inner class instance method')
if __name__ == '__main__':
	#approach-1
	#ref1=outer()
	#ref2=ref1.inner()
	#ref2.disp()

	#approach-2
	#ref=outer().inner()
	#ref.disp()

	#approach-3
	#outer().inner().disp()

	#approach-4
	#outer.inner().disp()

