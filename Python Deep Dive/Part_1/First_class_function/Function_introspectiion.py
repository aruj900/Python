#Functions are first class objects

def my_func(a:"mandatory positional",
            b:"optional positional"= 1,
            c=2,
            *args: "add extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs:"provide extra kw-only here")-> "does nothing":
    """This function does nothing but does have various parameters
    and annotations."""
    i = 10
    j = 20
    
print(my_func.__annotations__)

my_func.short_description = "this is a function that does nothing much"

print(dir(my_func))

print(my_func.__name__)

print(id(my_func))

def func_call(f):
    print(id(f))
    print(f.__name__)

print(func_call(my_func))

import inspect 
from inspect import isfunction, ismethod, isroutine

a= 10

print(isfunction(a))

print(isfunction(my_func))

print(ismethod(my_func))

class MyClass:
    def f(self):
        pass
    
print(isfunction(MyClass.f))

my_obj = MyClass()

print(isfunction(my_obj.f))

print(ismethod(my_obj.f))

import inspect

print(inspect.signature(my_func))

sig = inspect.signature(my_func)

print(sig.parameters)

for k,param in sig.parameters.items():
    print('key:', k)
    print('Name:',param.name)
    print('Default:',param.default)
    print('Annotations',param.annotation)
    print('kind', param.kind)
    print('----------------------')
    
    
