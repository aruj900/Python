def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args,**kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args,**kwargs)
        print('{0}:called {1}'.format(run_dt,fn.__name__))
        return result 
    return inner


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


@logged
def func_1():
    pass

@logged
def func_2():
    pass

print(func_1())

print(func_2())

@logged
@timed
# when we stack decorators it behaves like this logged(timed(func)) timer will execute fit as it is inner func
def fact(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul,range(1,n+1))
print(fact(10))


