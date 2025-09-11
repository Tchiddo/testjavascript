# Write a program in which a user can enter an amount of pennies and the program will output the number of Dollars, Quarters, Dimes, Nickels and Pennies.

# Base Values
dollar_bill = 100
quarters = 25
dimes = 10
nickles = 5
pennies = 1

print ("-------------------------------------------------")

penny_deposit = int(input("Welcome to Pennies From Heaven.co customer! How many pennies would you like to deposit today? "))

print (f"Converting {penny_deposit} pennies. Please wait....")

# Value Calculation
post_dollar = int (penny_deposit // dollar_bill)
post_quarters = int (post_dollar // quarters)
post_dimes = int (post_quarters // dimes)
post_nickles = int (post_dimes // nickles)
post_pennies = int (post_nickles // pennies)

# The amount of money left after converting from specific currency
dollar_penny_deposit = int (penny_deposit - post_dollar * 100)
quarter_penny_deposit = int (dollar_penny_deposit - post_quarters * 25)
dime_penny_deposit = int (dollar_penny_deposit - post_dimes * 10)
nickle_penny_deposit = int (dime_penny_deposit - post_nickles * 5)
penny_penny_deposit = int (nickle_penny_deposit - post_pennies * 1)

print ("-------------------------------------------------")

def penny_conversion():
    if penny_deposit % dollar_bill == 0 :
        print (post_dollar) 

    elif penny_deposit % dollar_bill != 0 :
        print (post_dollar)
        print (int(dollar_penny_deposit / quarters ))
    
penny_conversion()






