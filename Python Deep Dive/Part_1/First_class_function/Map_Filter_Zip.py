def fact(n):
    return 1 if n < 2 else n * fact(n-1)


print(fact(3))


results = map(fact, range(6))

for x in results:
    print(x)

# Cant reuse because only calculate once use list() to store   

l1 = [1,2,3,4,5]

l2 = [10,20,30]

results = list(map(lambda x,y: x+y, l1, l2))

print(results)

x = range(25)

print(x)

print(list(filter(lambda x: x % 3 == 0,range(25))))


l1 = [1,2,3,4]
l2 = [10,20,30,40]
l3 = 'python'

results = list(zip(l1,l2,l3))

for x in results:
    print(x)

results = [fact(n) for n in range(10)]
print(results)

results = (fact(n) for n in range(10))
print(results)

for x in results:
    print(x)
    
l1 = [1,2,3,4,5,6]
l2 = [10,20,30,40]

print([x+y for x,y in zip(l1,l2)])

print(list(filter(lambda x: x%2==0,map(lambda x,y: x+y, l1,l2))))

print([x+ y for x,y in zip(l1,l2) if x%2 == 0])


