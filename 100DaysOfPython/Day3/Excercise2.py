height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in kg: "))

BMI = weight//(height**2)

if BMI < 18.5:
    print("You are underweight.")

elif BMI < 25:
    print("You are underweight.")

elif BMI < 30:
    print("You are overweight.")

elif BMI < 35:
    print("You are Obese.")
else:
    print("You are clinically obese")
