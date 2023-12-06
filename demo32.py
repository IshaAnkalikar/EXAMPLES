'''32. WAP to collect year of birth from the
 user and print their current age and retirement slot 
 using nested function 

'''
#My code 
#normal code
yob=int(input('Enter year of birth'))
ret_age=60
cur_yr=2023
cur_age=cur_yr-yob
print(cur_age)
ret_yrs_left_for_ret=ret_age-cur_age
print(ret_yrs_left_for_ret)

#Sir's code
def retirement_age(yob):
	data='Years left for retirement'
	def retirement(retirement_slot):
		age=(datetime.now().year)-yob
		print(f'age is {age}')
		print(f'{retirement_slot-age} {data}')
	return retirement
if __name__ == '__main__':
	from datetime import datetime
	ref=retirement_age(yob=2003)
	ref(retirement_slot=60)
	#del retirement_age
	#ref(retirement_slot=60)