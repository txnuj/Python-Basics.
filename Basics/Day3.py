#Math Functions.
x = 2.9
print(round(x)) #Rounding Off the value of 2.9 to 3

x = -2.9
print(abs(x))   #Returns the absolute value which is nothing but positive.

import math
print(math.ceil(2.9))   #Prints the ceiling value which is 3.
print(math.floor(2.9))  #Prints the floor value which is 2.

#If Statement.
is_hot = True
if is_hot:
    print("It's a hot day")
print("Enjoy your day")

is_hot = False
if is_hot:
    print("It's a hot day")
print("Enjoy your day")

is_hot = False
is_cold = True
if is_hot:
    print("It's a hot day")
    print("Drink plenty of water")
elif is_cold:
    print("It's a cold day")
    print("Wear warm clothes")
else:
    print("It's a lovely day")
print("Enjoy your day")

#Exercise 4.
house_price = 1000000
good_credit = True
if good_credit:
    down_payment = house_price * 10 / 100
else:
    down_payment = house_price * 20 / 100
print(f"Down Payment: ${down_payment}")

#Logical Operators.
high_income = True
good_credit = True

if high_income and good_credit:     #AND: Both condition must be True.
    print("Eligible for Loan")
elif high_income or good_credit:    #OR: Atleast one condition must be True.
    print("Not Enough for Loan")
elif high_income and not good_credit:   #NOT: Reciprocate the given False statement to True.
    print("Eligible for Loan")

#Comparison Operators.
temperature = 35
if temperature > 30:
    print("It's a hot day")
else:
    print("It's not a hot day")

#Exercise 5.
first_name = "Tanuj"
if len(first_name) < 3:
    print("Name must be atleast 3 character long")
elif len(first_name) > 50:
    print("Name must be maximum of 50 character long")
else:
    print("Name looks good!")

#Weight Converter Program.
weight = int(input("Enter Your Weight: "))
unit = input("(L)bs or (K)gs:")
if unit.upper() == 'L':
    convert = weight * 0.45
    print(f"Yor are {convert} in kilos")
else:
    convert = weight / 0.45
    print(f"You are {convert} in pounds")

