import art
import game_data
import random
import os

def clear():
    os.system('cls||clear')


Comparison_one = random.choice(game_data.data)

Comparison_two = random.choice(game_data.data)
if Comparison_one == Comparison_two:
    Comparison_two = random.choice(game_data.data)

score = 0

win = True 
print(art.logo)
while win:
    print(f"Comapre A: {Comparison_one['name']}, a {Comparison_one['description']}, from {Comparison_one['country']}")
    print(art.vs)
    print(f"Compare B: {Comparison_two['name']}, a {Comparison_two['description']}, from {Comparison_two['country']}")
    user_selection = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_selection == 'a' and Comparison_one['follower_count'] > Comparison_two['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        Comparison_one = Comparison_two
        Comparison_two = random.choice(game_data.data)
        if Comparison_one == Comparison_two:
            Comparison_two = random.choice(game_data.data)
    elif user_selection == 'a' and Comparison_one['follower_count'] < Comparison_two['follower_count']:
        print(f"Sorry that's wrong! Final score: {score}")
        win = False
        break;
        
    elif user_selection == 'b' and Comparison_one['follower_count'] > Comparison_two['follower_count']:
        print(f"Sorry that's wrong! Final score: {score}")
        win = False
        break;
        
    elif user_selection == 'b' and Comparison_one['follower_count'] < Comparison_two['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        Comparison_one = Comparison_two
        Comparison_two = random.choice(game_data.data)
        if Comparison_one == Comparison_two:
            Comparison_two = random.choice(game_data.data)
        
        
        