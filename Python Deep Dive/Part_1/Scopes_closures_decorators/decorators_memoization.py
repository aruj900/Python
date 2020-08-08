def fib(n):
    print('Calculating fib({0})',format(n))
    return 1 if n < 3 else fib(n-1) +fib(n-2)

class Fib:
    
    def __init__(self):
        self.cache = {1:1,2:1}
    
    def fib(self,n):
        if n not in self.cache:
            print('Calculating fib({0})',format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
        return self.cache[n]

f = Fib()
print(f.fib(10))
print(f.fib(12))

# Now we will do same using closures


def fib():
    cache = {1:1,2:1}
    
    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})',format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]
    return calc_fib

f = fib()
print(f(10))
print(f(12))

def memo_fib(fn):
    #cache = {1:1,2:1}
    cache = dict()
    
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)
        return cache[n]
    return inner

@memo_fib
def fib(n):
    print('Calculating fib({0})',format(n))
    return 1 if n < 3 else fib(n-1) +fib(n-2)

print(fib(10))
print(fib(12))

@memo_fib
def fact(n):
    print('Calculating fact({0})',format(n))
    return 1 if n < 2 else n*fact(n-1)

print(fact(6))
print(fact(7))


from functools import lru_cache
# This does whatver we did above
@lru_cache()
def fib2(n):
    print('calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib2(10))
print(fib2(12))

# we can set maxsize of the cache
@lru_cache(maxsize=8)
def fib3(n):
    print('calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print(fib3(8))
print(fib3(9))
print(fib3(1))

