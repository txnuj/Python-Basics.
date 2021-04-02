#While Loops
i = 1
while i <=5:    #Condition works until i value is less than or equal to 5.
    print(i)
    i = i+1
print("Done")

i = 1
while i <=5:    #Condition works until i value is less than or equal to 5.
    print("*" * i)  #Prints * values with respect to i value.
    i = i+1
print("Done")

#Guessing Game.
secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess: "))
    guess_count += 1
    if guess == secret_number:
        print("You are Right!")
        break
else:
    print("Better Luck Next Time")

#Car Game
command = ""
started = False
stopped = False
while command != "quit":
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car's already started, ready to go!")
        else:
            started = True
            print("Car started, ready to go")
    elif command == "stop":
        if stopped:
            print("Car has already stopped!")
        else:
            stopped = True
            print("Car stopped")
    elif command == "help":
        print("""
        start - To start the car
        stop - To stop the car
        quit - To quit the car""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand")

#For Loops.
for i in "Python":  #Prints character by character
    print(i)

for i in ["Tanuj", "Sudhire", "Raja"]:  #Prints the item's inside the Square Brackets
    print(i)

for i in range(10): #Prints 0 to 9 which is in the range of 10.
    print(i)

for i in range(5,10): #Prints 5 to 9 which is in the range of 10.
    print(i)

for i in range(5,10,2): #Prints 5 to 9 and skips 2 numbers in between.
    print(i)

#Exercise 6.
prices = [10, 20, 30]
sum = 0
for i in prices:
    sum += i
print(f"Total is: {sum}")

#Nested Loop.
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

#Challenge
numbers = [5, 2, 5, 2, 2]
for item in numbers:
    count = ""
    for i in range(item):
        count += 'X'
    print(count)

#Lists.
names = ["Josh", "Bob", "Mosh", "Sarah", "Mary"]
print(names[0])     #Prints John.

#Exercise 7.
numbers = [10, 20, 30, 40, 50]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(f" Max number in the Lists is: {number}")





