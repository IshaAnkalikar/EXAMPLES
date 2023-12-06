'''WAP to merge characters of two strings into a single 
string by taking characters alternatively 
input: s1="ravi"
       s2="teja"
output:rtaevjia
'''

s1="ravi"
s2="teja"
print(s1)
print(s2)
res=''
i,j=0,0
while i<len(s1) and j<len(s2):
	if i<len(s1):
		res=res+s1[i]
		i=i+1
	if j<len(s2):
		res=res+s2[j]
		j=j+1
print(res)