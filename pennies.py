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
dollar_penny_deposit = int (penny_deposit - post_dollar * dollar_bill)
quarter_penny_deposit = int (dollar_penny_deposit - post_quarters * quarters)
dime_penny_deposit = int (dollar_penny_deposit - post_dimes * dimes)
nickle_penny_deposit = int (dime_penny_deposit - post_nickles * nickles)
penny_penny_deposit = int (nickle_penny_deposit - post_pennies * pennies)

dollar_true = penny_deposit % dollar_bill == 0
quarter_true =dollar_penny_deposit % quarters == 0
dime_true = quarter_penny_deposit % dimes == 0
nickle_true = dime_penny_deposit % nickles == 0
penny_true = nickle_penny_deposit % pennies == 0

print ("-------------------------------------------------")

def penny_conversion():
    if   dollar_true :
        print (f"{post_dollar} dollars") 
    
    elif quarter_true :
        print (f"{post_dollar} Dollars")
        print (f"{dollar_penny_deposit // quarters} Quarters")
    
    elif dime_true :
        print (f"{post_dollar} Dollars")
        print (f"{dollar_penny_deposit // quarters} Quarters")
        print (f"{quarter_penny_deposit // dimes} Dimes")
    
    elif nickle_true :
        print (f"{post_dollar} Dollars")
        print (f"{dollar_penny_deposit // quarters} Quarters")
        print (f"{quarter_penny_deposit // dimes} Dimes")
        print (f"{dime_penny_deposit // nickles} Nickles")

    elif penny_true :
        print (f"{post_dollar} Dollars")
        print (f"{dollar_penny_deposit // quarters} Quarters")
        print (f"{quarter_penny_deposit // dimes} Dimes")
        print (f"{dime_penny_deposit // nickles} Nickles")
        print (f"{nickle_penny_deposit // pennies} Pennies")


    
penny_conversion()



