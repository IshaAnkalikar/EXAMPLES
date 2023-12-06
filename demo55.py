#super class method
#syntax: super(childclassname,self).parentclassmethodname()
class parent:
	def wish(self):
		print('My kid should become an engg')
class child(parent):
	def wish(self):
		print('I wish to become an actor')
		super(child,self).wish()
if __name__ == '__main__':
	c=child()
	c.wish()