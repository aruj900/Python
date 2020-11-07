print("Welcome to tip calculator")
Total_bill = input("What was the total bill? ")
Tip = input("What percentage tip would you like to give? 10, 12 or 15? ")
People = input("How many people to split the bill? ")

Bill = float(Total_bill) + (int(Tip)/100 * float(Total_bill))
each_bill = Bill / int(People)
print(f"Each person should pay: ${each_bill}")