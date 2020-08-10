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

d2 = Data(*data_dict.values())

print(d2)

key_name = 'key2'

# Use getattr for key

print(getattr(d2, key_name))


data_list = [
    {'key1':1,'key2':2},
    {'key1':3,'key2':4},
    {'key1':5,'key2':6,'key3':7},
    {'key2':100}
]

keys = set()
for d in data_list:
    for key in d.keys():
        keys.add(key)
        
print(keys)

keys = {key for dict_ in data_list for key in dict_.keys()}

print(keys)


Struct = namedtuple('Struct', sorted(keys))

print(Struct._fields)

Struct.__new__.__defaults__ = (None,)*len(Struct._fields)

tuple_list = []
for dict_ in data_list:
    tuple_list.append(Struct(**dict_))
print(tuple_list)


def tuplify_dicts(dicts):
    keys = {key for dict_ in dicts for key in dict_.keys()}
    Struct = namedtuple('Struct', sorted(keys), rename=True)
    Struct.__new__.__defaults__ = (None,) * len(Struct._fields)
    return [Struct(**dict_) for dict_ in dicts]

tuple_list = tuplify_dicts(data_list)

print(tuple_list)