a = (10,20,30)
b = 10,20,30

#Both are tuple

def print_tuple(t):
    for e in t:
        print(e)

# In this case we had to use parenthesis 

print(print_tuple((10,20,30)))

a = 1,2,3,4,5

x, *_,y,z = a

print(_)

class Point2D:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y ={self.y})'
    
pt = Point2D(x=10,y=20)

pt.x = 100

print(id(pt))

s = 'python' + ' rocks!'

print(s)

#Strings are immutable here s is a different variable with different id same for tuple

london = 'London', 'UK', 8_780_000
new_york = 'New York', 'USA', 8_500_000
beijing = 'Beijing', 'China', 21_000_000

cities = [london,new_york,beijing]

total = 0
for city in cities:
    total += city[2]
print(total)

total = sum(city[2] for city in cities)
print(total)

#we can use this for enumerate

for index,city in enumerate(cities):
    print(index,city)


from random import uniform
from math import sqrt

def random_shot(radius):
    random_x = uniform(-radius,radius)
    random_y = uniform(-radius,radius)
    
    if sqrt(random_x**2 + random_y**2) <= radius:
        is_in_circle = True
    
    else: 
        is_in_circle = False
        
    return random_x, random_y, is_in_circle

num_attempts = 100
count_inside = 0
for i in range(num_attempts):
    *_, is_in_circle = random_shot(1)
    if is_in_circle:
        count_inside += 1
print(f'Pi is approx : {4 * count_inside/num_attempts}')