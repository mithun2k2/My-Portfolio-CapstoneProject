import math

print ("Investment - To calculate the amount of interest you'll earn on your investment")
print("Bond - To calculate the amount you'll have to pay on a home loan")

User = input("Enter either 'investment' or 'bond' from the menu above to proceed: ").lower()

# Investment plan one of the condition 
if User == "investment":     
        initial_amount = float(input("How much are you depositing: \nGBP"))
        interest_rate = float(input("At which interest percentage rate: \n"))
        interest_rate = (interest_rate/100)
        number_of_years = float(input("How many yesrs are you planning to invest: \n"))
        investment_type = input("Choose Simple or Compound interest: \n").lower()
        
        if investment_type == "simple":
            "simple" == investment_type
            investment_type = initial_amount * (1 + interest_rate * number_of_years)
            total = investment_type
            print(f"Your interest earned over {number_of_years} years will be GBP {total: .2f}")
        elif investment_type:
            investment_type = initial_amount * math.pow((1 + interest_rate),number_of_years) 
            total = investment_type
            print (f"Your interest earned over {number_of_years} years will be GBP{total:.2f}")

#Bond is another conditional

elif User == "bond":
        
        current_value = float(input("What is the current value of the house?\nGBP")) 
        interest_rate = float(input("At which interest rate percentage?\n" )) 
        interest_rate = ((interest_rate / 100)/12)
        monthly_repay = float(input("How many months you plan to repay? \n")) 
        monthly = float(math.floor((interest_rate * current_value)/(1 - (1+interest_rate)**(-monthly_repay))))
        print(f"Your monthly repayment will be : {monthly:.2f}")
else:
    print("Please enter a valid input. Try again.")