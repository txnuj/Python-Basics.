#Type Conversion.
birth_year = input("What's your birth year? ")
print(type(birth_year))
age = 2020 - int(birth_year)
print(type(age))
print(age)

#Exercise 3.
weight = input("Enter your Weight in Pounds? ")
kg = float(weight) * 0.454
print("Your weight in Kg is: ")
print(kg)

#Multiple Quotes.
email = '''
Hey John
This is your first email
Hope you like it
Thank You,
The Support Team.
'''
print(email)

#Strings
course = 'Python For Beginners'
print(course[0])    #Prints the first letter of the string.
print(course[-1])   #Prints the last letter of the string.
print(course[0:5])  #Starts with 0 and goes upto 4 character's.
print(course[:])    #Prints all the string element.
print(course[:5])   #Assumes to be 0 and goes upto 4 character.

name = 'Jennifer'
print(name[1:-1])   #Starts with e goes all the way to e and excludes r.

#Formatted Strings.
first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
msg = f'{first} [{last}] is a coder'
print(message)
print(msg)

#String Methods.
course = 'Python for Beginners'
print(len(course))      #Returns the length of the string.
print(course.upper())   #Prints the course details in Upper Case.
print(course.lower())   #Prints the course details in Lower Case.
print(course.find('P')) #Returns the P place.
print(course.replace('Beginners', 'Absolute Beginners'))    #Replace Beginners to Absolute Beginners.
print('Python' in course)   #Returns in boolean as the string present in course or not.

#Arithmetic Operators.
print(10 + 3)
x = 10
x = x + 3   #Also be written as x += 3
print(x)

#Operator Precedence
x = 2 ** 2  #Exponential which is 2 power 2.
x = 2 * 2 or 2 / 2  #Multiplication or Division
x = 2 + 2 or 2 - 2  #Addition or Subtraction.

y = 10 + 3 * 2 ** 2
print(y)
