s = slice(0,2)
print(type(s))

print(s.start)

print(s.stop)

l = [1,2,3,4,5,6]

print(l[s])

print(l[0:100])

print(l[0:6:2])

print(slice(1,5))

s = slice(1,5)

print(s.indices(10))

print(slice(0,100,2).indices(10))

