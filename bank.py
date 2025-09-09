print ("-----------------------------------")

customer_name = input ("Welcome, what is your name? ")

starting_balance = 5000.25

# User input to tell their starting balance
print ("Hello" , customer_name , "your starting balance is" , starting_balance)

print ("-----------------------------------")

pay_check = float(input("How much of your paycheck would you like to deposit? "))

print ("-----------------------------------")

expenditure_items = (input("Looks like you went shopping recently. What did you buy? "))

expenditure = float(input("How much did " + expenditure_items + ", cost: "))

print ("-----------------------------------")

def checking_balance(user_name, balance, deposits, expense_item, expense_amount):
   
    ending_balance = balance + deposits - expense_amount

    print(f"Good day {user_name}. After spending {expense_amount} on {expense_item}, your current balance is: {ending_balance}")

checking_balance(customer_name, starting_balance, pay_check, expenditure_items, expenditure)

