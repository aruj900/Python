from random import randint, random
from collections import namedtuple

def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return red,green,blue,alpha

color = random_color()
print(color)

Color = namedtuple('Color', 'red green blue alpha')

#When we use named tuples it will show the fields in autocomplete editors
def random_color():
    red = randint(0, 255)
    blue = randint(0, 255)
    green = randint(0, 255)
    alpha = round(random(), 2)
    return Color(red,green,blue,alpha)

color = random_color()

print(color)

# Named sstuples can be used as alternative to dictonaries

from collections import namedtuple

data_dict = dict(key1=100,key2=200,key3=300)

data_dict['key1']

Data = namedtuple('Data', data_dict.keys())