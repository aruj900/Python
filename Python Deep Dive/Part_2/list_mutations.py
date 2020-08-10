l =[1,2,3,4,5]

print(id(l))

print(l[0])

suits = ['spades','Hearts','Diamonds','Clubs']

alias = suits

alias.clear()

print(suits)

l[0:2] = ('a','b','c','d')

print(l)

l = [1,2,3,4]

l = l + [5]

print(l)

# Id of l changes after concatination

#append and extend doesnt change the id

l = [1,2,3]


print(id(l))

l.extend([4,5,6])


print(id(l))

# if we extend using set order is not maintained

l = [1,2,3]
print(id(l))
l.extend({'X','a','A',100_000})

print(id(l))

# pop mutates and returns the element

result = l.pop()

print(result)

l.insert(1,'a')

del l[2]

print(l)

l = [1,2,3]

l.reverse()

print(l)
