'''
x=7
lst=[]
i=0
if i==0:
	lst.append(i)
print(lst)
if i==1:
	lst.append(i)
print(lst)
else:
	lst.append(fib(i-1)+fib(i-2))
print(lst)
'''


'''
18. WAP to generate the fibonacci sequence up to nth term
input: 7
output: [0,1,1,2,3,5,8,13]
logic: [prevnumber+curnumber=nextnumber]

'''
#without LC
num=7
prev,cur=0,1
print("fibonacci series:",prev,cur,end=" ")
for i in range(1,num):
	next_value=prev+cur
	prev=cur
	cur=next_value
	print(next_value,end=" ")
print()