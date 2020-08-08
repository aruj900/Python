def counter(fn):
    count = 0
    
    def inner(*args,**kwargs):
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
    
    return inner

def add(a:int,b:int = 0):
    """
    adds two values
    """
    return a + b

add = counter(add)

help(add)

print(add(10,20))

def mult(a:int,b:int,c:int = 1,*,d):
    """
    multiplies four values
    """
    return a*b*c*d

print(mult(1,2,3,d=4))

mult = counter(mult)

@counter
def my_func(s:str,i:int)->str:
    return s * i

print(help(my_func))

def counter1(fn):
    count = 0
    
    def inner(*args,**kwargs):
        """
        This is the inner closure
        """
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
    inner.__name__ = fn.__name__
    inner.__doc__ = fn.__doc__
    return inner

def mult(a:int,b:int,c:int = 1,*,d):
    """
    multiplies four values
    """
    return a*b*c*d

mult = counter1(mult)

print(help(mult))

from functools import wraps

def counter2(fn):
    count = 0
    
    #@wraps(fn)
    def inner(*args,**kwargs):
        """
        This is the inner closure
        """
        nonlocal count
        count += 1
        print('Function {0} was called {1} times'.format(fn.__name__,count))
        return fn(*args,**kwargs)
    inner = wraps(fn)(inner)
    return inner

def mult(a:int,b:int,c:int = 1,*,d):
    """
    multiplies four values
    """
    return a*b*c*d

mult = counter2(mult)
print(help(mult))


def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args,**kwargs):
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        elapsed = end - start
        
        