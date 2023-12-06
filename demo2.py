'''
2. WAP to reverse order of words
input:Learning python is very easy
output:
'''
s='Learning python is very easy'
print(s)
lst=s.split()
print(lst)
print(len(lst))
n=len(lst)-1


#without using reversed
s='Learning python is very easy'
print(s)
lst=s.split()
print(lst)
n=len(lst)-1
lst1=[]
while n>=0:
	lst1.append(lst[n])
	n=n-1
print(lst1)
print(' '.join(lst1))
