l1 = [1,2,3]
l1_copy = []

for item in l1:
    l1_copy.append(item)

print(l1_copy)
print(id(l1),id(l1_copy))

l1_copy = [item for item in l1]
print(l1_copy)

print(id(l1_copy))

l1_copy = l1.copy()

print(l1_copy)

print(id(l1))
print(id(l1_copy))

t1 = (1,2,3)

l1_copy = list(t1)

print(l1_copy)

t1 = (1,2,3)
t2 = tuple(t1)

print(id(t1))
print(id(t2))

# Since strings and tuples are immutable we get same id as python optimize this

import copy 
l1 = [1,2,3]
l2 = copy.copy(l1)

print(id(l1),id(l2))

t1 = (1,2,3)
t2 = copy.copy(t1)

print(id(t1),id(t2))

v1 = [0,0]
v2 = [0,0]

line1 = [v1,v2]

line2 = line1.copy()

print(id(line1),id(line2))

#Notice list of lists are pointing to same memory address
print(id(line1[0]),id(line2[0]))

line2 = [v for v in line1]

print(id(line1[0]),id(line2[0]))

#Now if we change first element of sublist it will change for line2 as well as it is shallow copy

line1[0][0] = 100

print(line1)
print(line2)

#This will create a deep copy of internal lists also
line2 = [v.copy() for v in line1]

print(line1)
print(line2)

print(id(line1),id(line2))


print(id(line1[0]),id(line2[0]))

line1[0][0] = -10
print(line1)
print(line2)

#Now suppose we have 3 level nesting this approach will fail so we can use deep copy function in python

v1 = [1,1]
v2 = [2,2]
v3 = [3,3]
v4 = [4,4]

line1 = [v1,v2]
line2 = [v3,v4]

plane1 = [line1,line2]
plane2 = copy.deepcopy(plane1)

print(id(plane1[0][0]),id(plane2[0][0]))

plane1[0][0][0] = 100
print(plane1)
print(plane2)

class Point:
    
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    
class Line:
    def __init__(self,p1,p2):
        self.p1 = p1
        self.p2 = p2
        
    def __repr__(self):
        return f'Line ({self.pi.__repr__()}, {self.p2.__repr__()})'
    
p1 = Point(0,0)
p2 = Point(10,10)

line1 = Line(p1,p2)
line2 = copy.deepcopy(line1)

print(line1.p1, id(line1.p1))
print(line2.p1, id(line2.p1))

# If we use only copy it will refer to same object