'''
9.WAP to get the following result
input: a4k3b2
output:aeknbd
'''
s='a4k3b2'
print(s)
res=''
for i in s:
	if i.isalpha():
		res=res+i
		data=i 
	else:
		res=res+chr(ord(data)+int(i))
print(res)