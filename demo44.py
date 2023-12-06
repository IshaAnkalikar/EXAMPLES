#setters and getters in python
class student:
	#instance method-1
	#setter method
	def setName(self,name):
		self.name=name 

	#instance method-2
	#setter method
	def setMarks(self,marks):
		self.marks=marks

	#instance method-3
	#getter method
	def getName(self):
		return self.name 

	#instance method-4
	#getter method
	def getMarks(self):
		return self.marks 

if __name__ == '__main__':
	num=int(input('enter the number of students:'))
	for i in range(num):
		s=student()
		name=input('enter the name:')
		marks=int(input('enter the marks:'))
		s.setName(name=name)
		s.setMarks(marks=marks)
		print(f'The name of the student is {s.getName()} and the marks are {s.getMarks()}')

