#Exception handling in python 
#Example-1
print('Conn estd')
num1=int(input('Enter num1:'))
num2=int(input('Enter num2:'))
res=num1/num2
print(f'res is {res}')
print('Conn Terminated')
'''
#output:
#Normal Termination
Conn estd
Enter num1:10
Enter num2:2
res is 5.0
Conn Terminated

#abrupt Termiantion
Conn estd
Enter num1:10
Enter num2:0
ZeroDivisionError: division by zero
'''
#User defined exception handler
#Example-1
try:
	print('Conn estd')
	num1=int(input('Enter num1:'))
	num2=int(input('Enter num2:'))
	res=num1/num2
	print(f'res is {res}')
except:
	print('Some problem occured')
print('Conn Terminated')

#multi-except blocks
print('Conn estd')
try:
	num1=int(input('Enter num1:'))
	num2=int(input('Enter num2:'))
	res=num1/num2
	print(f'res is {res}')
except ZeroDivisionError:
	print('pls enter non-zero denominator')
except ValueError:
	print('pls enter valid integer')
except NameError:
	print('pls check the input once')
except TypeError:
	print('pls check the datatype of the input')
except:
	print('Some problem occured')
print('conn Terminated')

#grouping except blocks
print('Conn estd')
try:
	num1=int(input('Enter num1:'))
	num2=int(input('Enter num2:'))
	res=num1/num2
	print(f'res is {res}')
except(ZeroDivisionError,ValueError,NameError,TypeError):
	print('pls enter valid input')
except:
	print('Exception is handled')
print('Conn Terminated')
