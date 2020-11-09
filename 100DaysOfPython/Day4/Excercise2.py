import random

nameAsCSV = input("Give me everybody's name, separated by a comma. ")
names = nameAsCSV.split(",")
choice = random.randint(0,len(names) -1 )

print(f"{names[choice]} is going to buy the meal today!")
