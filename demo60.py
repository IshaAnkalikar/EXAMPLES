#GARBAGE COLLECTOR
#Example-1
if __name__ == '__main__':
	import gc
	print(f'The status of garbage collector is: {gc.isenabled()}')#true
	gc.disable()
	print(f'The status of garbage collector is: {gc.isenabled()}')#false
	gc.enable()
	print(f'The status of garbage collector is: {gc.isenabled()}')#true
	print(f'The status of garbage collector is: {gc.isdisabled()}')#error
	print(f'The status of garbage collector is: {gc.disable()}')#none

