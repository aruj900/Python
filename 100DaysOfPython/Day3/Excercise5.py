print("Welcome to love calculator!")
your_name = input("What is your name?")
their_name = input("What is their name?")
final_name = your_name.lower() + their_name.lower()
true_score = (final_name.count("t") + final_name.count("r") + final_name.count("u") + final_name.count("e")) * 10
love_score = (final_name.count("l") + final_name.count("o") + final_name.count("v") + final_name.count("e"))
final_score = true_score + love_score

if final_score < 10 or final_score > 90:
    print(f"Your score is {final_score}, you go together like coke and mentos.")

elif final_score > 40 and final_score < 50:
    print(f"Your score is {final_score}, you are alright together")

else:
    print(f"Your score is {final_score}") 
