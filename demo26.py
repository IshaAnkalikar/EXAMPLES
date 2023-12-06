'''
26.WAP to find the factorial of a given number
input: 5
output: 5 fact is 120
'''
'''

#MY CODE
def fun(n):
	if n==0:
		print('fact of',n,'is',1)
	else:
		fact=n*fact(n-1)
	return fact

if __name__ == '__main__':
	n=int(input('Enter a number:'))
	res=fun(n)
	print(res)	
'''


#SIR'S CODE
def fact(n):
	if n==1:
		return 1
	else:
		return n*fact(n-1)
if __name__ == '__main__':
	n=int(input('Enter a num:'))
	res=fact(n)
	print(res)