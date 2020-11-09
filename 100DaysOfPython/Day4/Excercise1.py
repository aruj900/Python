import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
Coin_toss = random.randint(0,1)

if Coin_toss == 1:
    print("Heads")
else:
    print("Tails")