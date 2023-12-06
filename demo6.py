''' 
6.WAP to sort the characters of strings and first 
alphabet symbols followed by numeric values
input:b4a1d3
output:abd134
'''
s='b4a1d3'
print(s)
s1=s2=res=''
for i in s:
	if i.isalpha():
		s1=s1+i
	else:
		s2=s2+i 
print(s1)
print(s2)
for i in sorted(s1):
	res=res+i 
for i in sorted(s2):
	res=res+i 
print(res)
