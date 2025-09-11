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

print ("-------------------------------------------------")

def penny_conversion():
    if penny_deposit % dollar_bill == 0 :
        print (post_dollar)
    elif penny_deposit / dollar_bill != 0 :
        print (post_dollar)

    if post_dollar % quarters == 0 :
        print (post_quarters)
    elif post_dollar / quarters != 0 :
        print (post_quarters)

penny_conversion()






