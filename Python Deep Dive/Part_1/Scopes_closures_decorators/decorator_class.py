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