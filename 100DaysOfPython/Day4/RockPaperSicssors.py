import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

rps = [rock,paper,scissors]

print("Welcome to rock, paper, scissors")
player_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper and 2 for scissors. "))
computer_choice = random.randint(0,2)
print(rps[player_choice])
print("Computer choose ")
print(rps[computer_choice])

if player_choice == 0 and computer_choice == 0:
    print("It's a draw") 
elif player_choice == 0 and computer_choice == 1:
    print("computer won") 
elif player_choice == 0 and computer_choice == 2:
    print("player won")

elif player_choice == 1 and computer_choice == 0:
    print("player won") 
elif player_choice == 1 and computer_choice == 1:
    print("It's a draw") 
elif player_choice == 1 and computer_choice == 2:
    print("computer won")

elif player_choice == 2 and computer_choice == 0:
    print("computer won") 
elif player_choice == 2 and computer_choice == 1:
    print("player won") 
else:
    print("It's a draw") 


