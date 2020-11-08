Year = int(input("Enter the year."))
if Year % 4 == 0 and Year % 100 != 0:
    print("It is a leap year")
elif Year % 4 == 0 and Year % 100 == 0 and Year % 400 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")