'''
22. WAP to 
'''
#MY CODE
'''
lst=input('enter the elements')
print(lst)
lst1=[]
def num(lst):
	for i in lst:
		if i%2==0:
			lst1.append(i**2)
		else:
			lst1.append(i**3)
	return lst1
if __name__ == '__main__':
	print(num(lst1))
	'''



	#SIR'S CODE
def fun(lst):
	lst1=[]
	for i in lst:
		if i%2==0:
			lst1.append(f'even {i**2}')
		else:
			lst1.append(f'odd {i**3}')
	return lst1
if __name__ == '__main__':
	lst=list(eval(input('Enter the elements: ')))
	print(lst)
	res=fun(lst)
	print(res)



