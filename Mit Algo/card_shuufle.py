cards = []
for i in range(1,53):
    cards.append(i)
    
def shuffle(cards):
    shuffled = []
    mid_card = len(cards)//2
    top_half = cards[0:mid_card]
    bottom_half = cards[mid_card:(len(cards))]
    
    for i in range(len(top_half)):
        shuffled.append(bottom_half[i])
        shuffled.append(top_half[i])
    return shuffled

#Top card after 7th shuffle
cards1 = cards
for i in range(7):
    first_shuffle = shuffle(cards1)
    cards1 = first_shuffle
    
print(cards1[0])

#top card become bottom after?
cards2 = cards
i = 0
next = True
while next:
    first_shuffle = shuffle(cards2)
    cards2 = first_shuffle
    i += 1
    if cards2[-1] == 1:
        next = False
    
print(i)
    
# when do first and last card touch?
cards3 = cards
i = 0
next = True
while next:
    first_shuffle = shuffle(cards3)
    cards3 = first_shuffle
    i += 1
    for j in range(52):
        if ((cards3[j] == 1 and cards3[j+1] == 52) or (cards3[j] == 1 and cards3[j-1] == 52)):
            next = False
    
print(i)
    

"""
first_shuffle = shuffle(cards)
second_shuffle = shuffle(first_shuffle)
third_shuffle = shuffle(second_shuffle)
fourth_shuffle = shuffle(third_shuffle)
fifth_shuffle = shuffle(fourth_shuffle)
sixth_shuffle = shuffle(fifth_shuffle)
seventh_shuffle = shuffle(sixth_shuffle)

print(seventh_shuffle)
"""




