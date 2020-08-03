def timed(fn):
    from time import perf_counter
    from functools import wraps
    
    @wraps(fn)
    def inner(*args,**kwargs):
        start = perf_counter()
        result = fn(*args,**kwargs)
        end = perf_counter()
        elapsed = end - start
        
        args_ =  [str(a) for a in args]
        kwargs_ = ['{0}={1}'.format(k,v) for (k,v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)
        
        print('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__,args_str,elapsed))
        
        return result
    return inner

#@timed
def fib_rec(n):
    if n <= 2:
        return 1
    else:
        return fib_rec(n-1) + fib_rec(n-2)

@timed
def fib(n):
    return fib_rec(n)

print(fib(7))
#print(fib(37))


@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3,n+1):
        fib_1,fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(fib_loop(7))


from functools import reduce

@timed
def fib_reduce(n):
    initial = (1,0)
    dummy = range(n)
    fib_n = reduce(lambda prev,n:(prev[0] +prev[1],prev[0]),dummy,initial)
    
    return fib_n[0]

print(fib_reduce(7))
        