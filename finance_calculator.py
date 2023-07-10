
# this is an example of  a python program calculating simple interest , compound interest or repayment
# the user input either investment or bond 
# The program output the appropriate amount they get after the given period depending on their options


import math

print("investment-to calculate the amount of interest you will earn on your investment")
print("bond- to calculate the amount you will have to pay on a home loan\n")

user_input=input("Enter either investment or bond from the menu above to proceed: ")

if user_input.upper()=="INVESTMENT":
	principal=float(input("Enter the amount you are depositing: "))
	interest_rate=float(input("Enter the interest rate: "))
	time=int(input("enter the number of years you are planning on investing: \n"))
	interest=input("please enter either simple or compound interest: ")

	if interest.lower()=="simple":
		total_amount=principal*(1+(interest_rate*time))
		print(f"balance after {time} years is:R{total_amount:2f}")
    
	elif interest.lower()=="compound":
		total_amount=principal*math.pow((1+interest_rate),time)
		print(f"balance after {time} years is:R{total_amount:2f}")
		
if user_input.upper()=="BOND":
	present_value=float(input("enter the amount of the present value: "))
	interest_rate=float(input("enter the interest rate: "))
	time=int(input("enter the number of months you are planning on repaying: \n"))
	
	repayment=(interest_rate*present_value)/(1-(1+interest_rate)**(-time))
	print(f"balance after {time} years is:R{repayment:2f}")
	
	
		
		
	
	
