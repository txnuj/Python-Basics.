#Generating Random Numbers.
import random

for i in range(3):
    print(random.random())

for i in range(3):
    print(random.randint(10,20))

names =  ["John","Mary","Smith","Mosh"]
leader = random.choice(names)
print(leader)

#Exercise 8.
import random

class Dice:
    def roll(self):
        roll = random.randint(1,6)
        roll2 = random.randint(1,6)
        return(roll,roll2)


dice1 = Dice()
print(dice1.roll())

#Working with Directories.
from pathlib import Path

#path = Path("Hi Hello")
#print(path.mkdir())        #Creates a new Directory.

#path = Path("Hi Hello")
#print(path.rmdir())        #Removes the created Directory.

path = Path()
print(path.glob("*.py"))

for file in path.glob("*.py"):
    print(file)


