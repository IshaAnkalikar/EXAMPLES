'''
4.WAP to print characters at odd position and even 
position for the given string
1.using slicing 
2.without using slicing
input:'learning python is very easy'  
output:erigpto svr ay
	   lann yhni eyes
'''
#using slicing
s='learning python is very easy' 
print(s)
print(s[1::2]) #at odd pos
print(s[::2]) #at even pos

#without using slicing
s='learning python is very easy' 
print(s)
n=len(s)
x=0
print('char at even pos')
while x<n:
	print(s[x],end=' ')
	x=x+2
print()
x=1
print('char at odd pos')
while x<n:
	print(s[x],end=' ')
	x=x+2
print()