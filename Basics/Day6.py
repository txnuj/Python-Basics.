#Keyword Arguements
def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}!")
    print("Welcome Aboard")


print("Start")
greet_user(last_name="John",first_name="Smith")     #Even though John takes the first_name, after using keyword arguements they can be sorted.
print("Finish!")

#Return Statements.
def square(number):
    return number * number

result = square(3)
print(result)

#Reusable Function.
def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😀",
        ":(": "😫",
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
result = emoji_converter(message)
print(result)

#Exceptions.
age = int(input("Enter your Age:"))
print(age)

try:
    age = int(input("Enter your Age:"))
    print(age)
except ValueError:      #If catches this kind of error, it prints the "Invalid User".
    print("Invalid Value.")

try:
    age = int(input("Enter your Age:"))
    income = 20000
    res = income / age
    print(age)
except ZeroDivisionError:       #If catches ZeroDivisionError, it prints "Age cannot be 0".
    print("Age cannot be 0")
except ValueError:
    print("Invalid Value.")

#Comments.
print("Sky is Blue.")   #Adding short note about the line of code for user understanding.

#Classes.
class Point:
    def draw(self):
        print("Draw!")

    def move(self):
        print("Move!")


point1 = Point()
point1.draw()
point1.x = 10
point1.y = 20
print(point1.x)

#Constructors.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def draw(self):
        print("Draw!")

    def move(self):
        print("Move!")


point1 = Point(10, 20)
print(point1.x)

#Exercise 8.
class Person:
    def __init__(self, name):
        self.name = name
    def talk(self):
        print(f"Hi, I'm {self.name}")

Name = Person("John Smith")
Name.talk()

#Inheritance.
class Mammal:
    def walk(self):
        print("Walk")


class Dog(Mammal):
    def bark(self):
        print("Bark")


class Cat(Mammal):
    def scratch(self):
        print("Scratch")


dog1 = Dog()
dog1.bark()
cat1 = Cat()
cat1.walk()

