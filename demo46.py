#single inheritance
#example-1
class Parent:
	def father(self):
		print('My son will obey my order')
class child(Parent):
	def son1(self):
		print('I will obey my fathers order')
	def son2(self):
		print('Who cares...!')
if __name__ == '__main__':
	c=child()
	c.son1()
	c.son2()
	c.father()