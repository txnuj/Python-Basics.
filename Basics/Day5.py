#2D Lists.
matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
print(matrix[0])    #Prints First row of Matrix.
print(matrix[0][2]) #Prints Second value in First row of matrix.

for row in matrix:
    for item in row:
        print(item)

#List Methods.
numbers = [5,2,1,7,4]
numbers.append(20)  #Adds 20 to the existing list
print(numbers)

numbers.insert(0,10)#Adds 10 to the first place of the existing list.
print(numbers)

numbers.remove(5)   #Removes 5 from the existing list.
print(numbers)

numbers.clear()     #Clears the list of values
print(numbers)

numbers = [5,2,1,7,4]
numbers.pop()       #Removes the last item in the list.
print(numbers)

print(50 in numbers)    #Returns boolean values

numbers.sort()      #Sort the numbers in ascending order.
print(numbers)

numbers.reverse()   #Sort the numbers in descending order.
print(numbers)

numbers = [5,3,7,6,1]
numbers2 = numbers.copy()   #Copy the existing values to another name.
numbers.append(50)
print(numbers)
print(numbers2)

#Write a program to remove duplicates in a list.
numbers = [2,2,4,6,3,4,6,1]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

#Tuples.
numbers = (1,2,3)
print(numbers[0])

#Unpacking
coordinates = (1,2,3)
x,y,z = coordinates
print(x,y,z)

#Dictionaries.
customer = {
    "Name": "John Smith",
    "Age": 30,
    "is_verified": True
}
print(customer['Name'])     #Prints the Name as John Smith.
print(customer.get("Birth Date"))   #Gets the value from the dictionary, if not returns None.

#Exercise 7.
phone = input("Phone:")
digits = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits.get(ch,"!") + " "
print(output)

#Emoji Converter.
message = input(">")
words = message.split(' ')
emojis = {
    ":)": "😀",
    ":(": "😫",

}
output = ""
for word in words:
    output += emojis.get(word, word) + " "
print(output)

#Functions.
def greet_user():
    print("Hi There")
    print("Welcome Aboard!")

print("Start")
greet_user()
print("Finish!")

#Parameters.
def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome Aboard")

print("Start")
greet_user("John")
print("Finish")
