import time

def time_it(fn,*args,**kwargs):
    print(args,kwargs)

time_it(print,1,2,3,sep="-",end='***')

def time_it(fn,*args,**kwargs):
    print(args,kwargs)
    
time_it(print,1,2,3, sep='-', end= ' ***')


def time_it(fn,*args,rep=1,**kwargs):
    for i in range(rep):
        fn(*args,**kwargs)

time_it(print,1,2,3, sep='-',end='***\n', rep=5)


def time_it(fn,*args,rep=1,**kwargs):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args,**kwargs)
    end = time.perf_counter()
    return (end-start)/rep

print(time_it(print,1,2,3, sep='-',end='***\n', rep=5))


def compute_powers_1(n,*,start=1,end):
    results = []
    for i in range(start,end):
        results.append(n**i)
    return results

print(compute_powers_1(2,end=5))

def compute_powers_2(n,*,start=1,end):
    # using list comprehension
    return [n**i for i in range(start,end)]

print(compute_powers_2(2,end=5))

def compute_powers_3(n,*,start=1,end):
    # using generators
    return (n**i for i in range(start,end))

print(list(compute_powers_3(2,end=5)))

print(time_it(compute_powers_1,2,start=0,rep=5,end= 20000))

print(time_it(compute_powers_2,2,start=0,rep=5,end= 20000))

print(time_it(compute_powers_3,2,start=0,rep=5,end= 20000))

#Generators doesn't calculate without list