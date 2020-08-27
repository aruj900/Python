l1 = [1,2,3,4]
l2 = [5,6]

print(id(l1),l1)
print(id(l2),l2)

l1 = l1 + l2

print(id(l1),l1)

t1 = (1,2,3)
#l1 = l1 + t1

l1 = [1,2,3,4]
l2 = [5,6]
t1 = (7,8)
print(id(l1),l1)
print(id(l2),l2)

l1 += l2
# This is in place concatination
print(id(l1),l1)

l1 += t1
print(id(l1),l1)

