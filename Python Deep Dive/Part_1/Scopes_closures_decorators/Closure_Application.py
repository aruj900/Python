class Averager:
    
    def __init__(self):
        self.numbers = []
    
    def add(self,number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total/count

a = Averager()

a.add(10)

print(a.add(20))
    
def averager():
    numbers = []
    def add(number):
        numbers.append(number)
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add

a = averager()

print(a(10))
print(a(30))



def averager():
    total = 0
    count = 0
    numbers = []
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total/count
    return add

a = averager()

print(a(10))
print(a(30))

from time import perf_counter
class Timer:
    def __init__(self):
        self.start = perf_counter()
    
    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()

print(t1())


def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll


t2 = timer()

print(t2())


def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()
print(counter1())

def counter(fn):
    cnt = 0
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has been called {1} times'.format(fn.__name__,cnt))
        return fn(*args,**kwargs)
    return inner

def add(a,b):
    return a + b

def mult(a,b):
    return a*b

counter_add = counter(add)

print(counter_add.__closure__)

result = counter_add(10,20)
print(result)

counter_mul = counter(mult)

print(counter_mul(2,5))

counters = dict()

def counter(fn,counters):
    cnt = 0
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args,**kwargs)
    return inner
c = dict()
counter_add = counter(add,c)
counter_mult = counter(mult,c)

print(counter_add(10,20))

print(counter_add(20,30))

print(counter_mult(10,20))

print(counter_mult(20,30))

print(counters)

def fact(n):
    product = 1
    for i in range(2,n+1):
        product *= i
    return product

counted_fact = counter(fact,c)

counted_fact(5)
print(c)