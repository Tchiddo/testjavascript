var_1 = input ("Please enter your first number: ") #Takes data in as a string
var_2 = input ("Please enter your second number: ") #Takes data in as a string
# Addidng these two wont work because they are strings. You gotta make them into a float

var_1 = float (var_1)
var_2 = float (var_2)

sum = var_1 + var_2
print (f"The sum of {var_1} + {var_2} = {sum}")

difference = var_1 - var_2
print (f"{var_1} * {var_2} = {difference}")

product = var_1 * var_2
print (f"{var_1} * {var_2} = {product}")

quotient = var_1 / var_2
print (f"{var_1} * {var_2} = {quotient}")

the_power = var_1 ** var_2
print(f"{var_1} ** {var_2} = {the_power}")