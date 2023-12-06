'''
25.WAP TO get required output
input:lst1=[10,20,30,40]
		lst2=[100,200,300,400]
output:
[10,400,20,300,30,200,40,100]
'''
'''
#MY CODE
def fun(lst1,lst2):
	lst3=[]
	for i in lst1:
		lst3.append(lst1[0:4])
	for i in lst2:
		lst3.append(lst2[-1:-5])
	return lst3
if __name__ == '__main__':
	lst1=[10,20,30,40]
	lst2=[100,200,300,400]
	print(lst1)
	print(lst2)
	res=fun(lst1,lst2)
	print(res)
	'''


	#SIR'S CODE
def fun(lst1,lst2):
		lst3=[]
		for x,y in zip(lst1,lst2[::-1]):
			lst3.extend([x,y])
		return lst3

if __name__ == '__main__':
		lst1=[10,20,30,40]
		lst2=[100,200,300,400]
		print(lst1)
		print(lst2)
		res=fun(lst1,lst2)
		print(res)