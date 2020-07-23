#Beware of using a mutable object for an argument default
from datetime import datetime
print(datetime.utcnow())

def log(msg,*,dt=datetime.utcnow()):
    print('{0}: {1}'.format(dt,msg))

print(log('message 1',dt ='2001-01-01 00:00:00.000'))

print(log('message 2'))


print(log('message 3'))

def log(msg,*,dt=None):
    dt = dt or datetime.utcnow()
    print('{0}: {1}'.format(dt,msg))

print(log('message 3'))



def add_item(name,quantity,unit,grocery_list):
    grocery_list.append("{0} ({1} {2}".format(name,quantity,unit))
    return grocery_list

store1 = []
store2 = []

add_item('banana',2,'units', store1)
add_item('milk',1,'liter',store1)

print(store1)

add_item('python',1,'medium-rare',store2)

print(store2)

def add_item(name,quantity,unit,grocery_list=[]):
    grocery_list.append("{0} ({1} {2}".format(name,quantity,unit))
    return grocery_list

del store1
del store2

store1 = add_item('banana',2,'units')
add_item('milk',1,'liter',store1)

print(store1)

store2 = add_item('python',1,'medium-rare')

print(store2)

print(store1)



def add_item(name,quantity,unit,grocery_list=None):
    if not grocery_list:
        grocery_list = []
    grocery_list.append("{0} ({1} {2}".format(name,quantity,unit))
    return grocery_list

del store1
del store2

store1 = add_item('banana',2,'units')
add_item('milk',1,'liter',store1)

print(store1)

store2 = add_item('python',1,'medium-rare')

print(store2)

print(store1)
print(store1 is store2)


def factorial(n):
    if n < 1:
        return 1
    else:
        print('calculation {0}!'.format(n))
        return n*factorial(n-1)

print(factorial(5))


def factorial(n,cache={}):
    if n < 1:
        return 1
    elif n in cache:
        return cache[n]
    else:
        print('calculation {0}!'.format(n))
        result = n*factorial(n-1)
        cache[n] = result
        return result
    
print(factorial(4))
print(factorial(5))

