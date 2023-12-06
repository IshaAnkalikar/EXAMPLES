'''1. WAP to reverse a string by using
 slicing operator and without using slicing operator.
'''
#using slicing :
s='learning python is easy'
print(s)
print(s[::-1])

#without using slicing;using while loop
s='learning python is easy'
print(s)
n=len(s)-1
x=0
data=''
while n>=x:
	data=data+s[n]
	n=n-1
print(data)

#using built-in function
print(reversed(s))
print(''.join(reversed(s)))