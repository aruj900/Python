def my_dec(a,b):
    def dec(fn):
        def inner(*args,**kwargs):
            print("decorated function called: a= {0},b= {1}".format(a,b))
            return fn(*args,**kwargs)
        return inner
    return dec

@my_dec(10,20)
def my_func(s):
    print('Hello {0}'.format(s))
    
print(my_func('World'))


class MyClass:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __call__(self,c):
        print("called a = {0}, b={1}, c ={2}".format(self.a,self.b,c))
        
obj = MyClass(10,20)

print(obj.__call__(100))

print(obj(100))

class MyClass:
    
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def __call__(self,fn):
        def inner(*args,**kwargs):
            print("decorated function called: a= {0},b= {1}".format(self.a,self.b))
            return fn(*args,**kwargs)
        return inner

@MyClass(10,20)
def my_func(s):
    print('Hello {0}'.format(s))
    
print(my_func('World'))

#Python classes can be made into decorators using __call__ method


from fractions import Fraction

f = Fraction(2,3)

Fraction.speak = lambda  self, message: 'Fraction says: {0}'.format(message)

print(f.speak('This is late parrot'))

Fraction.is_integral = lambda self: self.denominator == 1

f1  = Fraction(2,3)
f2 = Fraction(64,8)

print(f2.is_integral())

def dec_speak(cls):
    cls.speak = lambda self,message: '{0} says: {1}'.format(self.__class__.__name__,message)
    return cls

Fraction = dec_speak(Fraction)
f1 = Fraction(2,3)

print(f1.speak('Hello'))

class Person:
    pass
Person = dec_speak(Person)

p = Person()

print(p.speak('this works!'))


from datetime import datetime,timezone


def info(self):
    results = []
    results.append('time: {0}'.format(datetime.now(timezone.utc)))
    results.append('Class:{0}'.format(self.__class__.__name__))
    results.append('id:{0}'.format(hex(id(self))))
    for k,v in vars(self).items():
        results.append('{0}: {1}'.format(k,v))
    return results

def debug_info(cls):
    cls.debug = info
    return cls

@debug_info
class Person:
    def __init__(self,name,birth_year):
        self.name = name
        self.birth_year = birth_year
        
    def say_hi():
        return 'Hello there!'

p = Person('John',1939)

print(p.debug())
 
@debug_info
class Automobile:
    def __init__(self,make,model,year,top_speed):
        self.make = make
        self.model = model
        self.year = year
        self.top_speed = top_speed
        self._speed = 0
        
    @property
    def speed(self):
        return self._speed
    
    @speed.setter
    def speed(self,new_speed):
        if new_speed > self.top_speed:
            raise ValueError('Speed cannot exceed top_speed.')
        else:
            self._speed = new_speed

favorite = Automobile('Ford','Model T',1908 ,45)

favorite.speed = 40

print(favorite.debug())


from math import sqrt

class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return 'Point({0},{1})'.format(self.x,self.y)
    
    def __eq__(self,other):
        if isinstance(other,Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __lt__(self,other):
        
        if isinstance(other,Point):
            return abs(self) < abs(other)
        
        else:
            return NotImplemented 
        
        
p1, p2, p3 = Point(2,3), Point(2,3), Point(0,0)

print(abs(p1))

print(p1 == p2)

print(p3 < p1)

# Greater than will also work as it is reflection of less than

def complete_ordering(cls):
    if '__eq__' in dir(cls) and '__lt__' in dir(cls):
        cls.__le__ = lambda self,other: self < other or self == other
        cls.__gt__ = lambda self,other: not(self < other) and not (self == other)
        cls.__ge__ = lambda self,other: not (self < other)
    return cls


@complete_ordering
class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return 'Point({0},{1})'.format(self.x,self.y)
    
    def __eq__(self,other):
        if isinstance(other,Point):
            return self.x == other.x and self.y == other.y
        else:
            return False
        
    def __lt__(self,other):
        
        if isinstance(other,Point):
            return abs(self) < abs(other)
        
        else:
            return NotImplemented 
        
        
p1, p2, p3 = Point(2,3), Point(2,3), Point(0,0)

print(p1 >= p2)


# As long as you have define one of the order others are created 
from functools import total_ordering

@total_ordering
class Point1:
    def __init__(self,x,y):
        self.x = x
        self.y = y
        
    def __abs__(self):
        return sqrt(self.x**2 + self.y**2)
    
    def __repr__(self):
        return 'Point({0},{1})'.format(self.x,self.y)
    
    def __lt__(self,other):
        
        if isinstance(other,Point1):
            return abs(self) < abs(other)
        
        else:
            return NotImplemented 
        
        
p1, p2, p3 = Point1(2,3), Point1(2,3), Point1(0,0)

print(p1 >= p2)