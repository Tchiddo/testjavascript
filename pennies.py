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
post_dollar = int(penny_deposit // dollar_bill)
dollar_penny_deposit = int(penny_deposit - post_dollar * dollar_bill)

post_quarters = int(dollar_penny_deposit // quarters)
quarter_penny_deposit = int(dollar_penny_deposit - post_quarters * quarters)

post_dimes = int(quarter_penny_deposit // dimes)
dime_penny_deposit = int(quarter_penny_deposit - post_dimes * dimes)

post_nickles = int(dime_penny_deposit // nickles)
nickle_penny_deposit = int(dime_penny_deposit - post_nickles * nickles)

post_pennies = int(nickle_penny_deposit // pennies)
penny_penny_deposit = int(nickle_penny_deposit - post_pennies * pennies)

# The amount of money left after converting from specific currency
dollar_penny_deposit = int (penny_deposit - post_dollar * dollar_bill)
quarter_penny_deposit = int (dollar_penny_deposit - post_quarters * quarters)
dime_penny_deposit = int (dollar_penny_deposit - post_dimes * dimes)
nickle_penny_deposit = int (dime_penny_deposit - post_nickles * nickles)
penny_penny_deposit = int (nickle_penny_deposit - post_pennies * pennies)


print ("-------------------------------------------------")

def penny_conversion():

    print(f"{post_dollar} Dollars")
    print(f"{post_quarters} Quarters")
    print(f"{post_dimes} Dimes")
    print(f"{post_nickles} Nickles")
    print(f"{post_pennies} Pennies")

penny_conversion()





