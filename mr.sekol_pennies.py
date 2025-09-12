
print ("Welcome to my Pennies From Heaven Application.")
print ("This program converts a total number of pennies into the fewest umber of dollar bills and coins.")

total_pennies = int(input("Enter the number of pennies that you have: "))


def pennies_to_change (total_pennies):

    dollars = total_pennies // 100 # Floor division (round down) to tell me max number of $1 bills in the change.
    total_pennies = total_pennies % 100

#Quarter Calc
    quarters = total_pennies // 25
    total_pennies = total_pennies % 25

# Dime Calc
    dimes = total_pennies // 10
    total_pennies = total_pennies % 10

# Nickle Calc
    nickels = total_pennies // 5
    total_pennies = total_pennies % 5

    remainder_pennies = total_pennies

    print (f"Dollars = {dollars}")
    print (f"Quarters = {quarters}")
    print (f"Dimes = {dimes}")
    print (f"Nickles = {nickels}")
    print (f"Pennies = {remainder_pennies}")

pennies_to_change (total_pennies)
