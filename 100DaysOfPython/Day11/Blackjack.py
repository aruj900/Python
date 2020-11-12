import art
import random
import os

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
def deal_card(cards):
    card = random.choice(cards)
    return card

def clear():
    os.system('cls||clear')

def calculate_score(two_cards):
    
    if sum(two_cards) == 21 and len(two_cards) == 2:
        return 0
    if 11 in two_cards and sum(two_cards) > 21:
        two_cards.remove(11)
        two_cards.append(1)
    
    return sum(two_cards)

def compare(user_score,computer_score):
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif user_score > 21:
        return "You went over. You lose"
    elif computer_score > 21:
        return "Opponent went over. You win"
    elif user_score > computer_score:
        return "You win"
    else:
        return "you lose"

def play_game():
    print(art.logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card(cards))
        computer_cards.append(deal_card(cards))


    while not is_game_over:

        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f" Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card(cards))
            else:
                is_game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card(cards))
        computer_score = calculate_score(computer_cards)

    print(f"Your final cards {user_cards} and score is {user_score}")
    print(f"Computer cards are {computer_cards} and score is {computer_score}")
    print(compare(user_score,computer_score))

while input("Do you want to play a game of blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()