print(callable(print))

print('hello')

result = print('hello')

print(result)

l =[1,2,3]

print(callable(l.append))

result = l.append(4)
print(l)

print(result)

s = 'abc'

print(callable(s.upper))

result = s.upper()
print(result)

from decimal import Decimal

print(callable(Decimal))

class MyClass1:
    def __init__(self,x=0):
        print('initializing......')
        self.counter = x

print(callable(MyClass1))

a = MyClass1(100)

print(a.counter)


class MyClass:
    def __init__(self,x=0):
        print('initializing......')
        self.counter = x

    def __call__(self,x=1):
        print('updating counter.............')
        self.counter += x

b = MyClass()

MyClass.__call__(b,10)

print(b.counter)

print(callable(b))