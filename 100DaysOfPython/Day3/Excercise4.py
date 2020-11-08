print("Welcome to python pizza Deliveries!")
size = input("What size of pizza do you want? S, M, or L ")
price = 0
if size == 'S':
    price = 15
elif size == 'M':
    price = 20
else:
    price = 25

pepperoni = input("Do you want pepperoni? Y or N ")
if size == 'S' and pepperoni == 'Y':
    price += 2
elif size == 'M' or size == 'L' and pepperoni == 'Y':
    price += 3

cheese = input("Do you want extra cheese? Y or N ")
if cheese == 'Y':
    price += 1

print(f"Your final bill is ${price}.")

