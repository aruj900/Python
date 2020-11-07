age = input("Enter your current age: ")
years = 90 - int(age)
days = years * 365
weeks = days // 7
months = years * 12

print(f"You have {days} days, {weeks} weeks and {months} months left")