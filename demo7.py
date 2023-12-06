'''
7.WAP for the following requirement
ihnput: a4b3c2
output:aaaabbbcc
'''
s='a4b3c2'
print(s)
res=''
for i in s:
	if i.isalpha():
		data=i
	else:
		res=res+data*int(i)
print(res)

