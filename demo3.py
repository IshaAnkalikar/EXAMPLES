'''
3. WAP to reverse internal content of each word
input:knowledge is power
output:
'''
s='knowledge is power'
print(s)
lst=s.split()
print(lst)
n=len(lst)-1
lst1=[]
x=0
while x<=n:
	lst1.append(lst[x][::-1])
	x=x+1
print(lst1)
print(' '.join(lst1))
