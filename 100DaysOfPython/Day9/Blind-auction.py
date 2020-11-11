import os
import art

print(art.logo)

def clear():
    os.system('cls||clear')

bids = {}
bidding = False


def find_highest(bids):
    highest_bid = 0
    for key in bids:
        bid_amount = bids[key]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = key
    print(f"The winner is {winner} with a bid of ${highest_bid}")

while not bidding:
    name = input("What is your name? ")
    bid = int(input("Enter the bid amount: $"))

    bids[name] = bid

    again = input("Are there any other users? yes or no ")
    if again == "no":
        bidding = True
        find_highest(bids)
    elif again == "yes":
        clear()


