def timed(fn,reps):
    from time import perf_counter
    
    def inner(*args,**kwargs):
        total_elapsed = 0
        for i in range(reps):
            
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)
        
        avg_run_time = total_elapsed/reps
        print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time,reps))
        return result
    return inner


def calc_fib_recurse(n):
    return 1 if n < 3 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)


#dec = timed(5)

#@dec
def fib(n):
    return calc_fib_recurse(n)


print(fib(20))

fib = timed(fib,5)

print(fib(28))


def dec_factory(a,b):
    print("running dec_factory")
    
    def dec(fn):
        print("running dec")
        
        def inner(*args,**kwargs):
            print("running inner")
            print("a={0},b{1}".format(a,b))
            return fn(*args,**kwargs)
        
        return inner
    return dec

dec = dec_factory(10,20)


@dec
def my_func():
    print("running my_func")
    
print(my_func())

@dec_factory(100,200)
def my_func():
    print("running my_func")
    
print(my_func)

my_func = dec_factory(150,250)(my_func)

def dec_factory1(reps):
    def timed(fn):
        from time import perf_counter
    
        def inner(*args,**kwargs):
            total_elapsed = 0
            for i in range(reps):
            
                start = perf_counter()
                result = fn(*args, **kwargs)
                end = perf_counter()
                total_elapsed += (end - start)
        
            avg_run_time = total_elapsed/reps
            print('Avg run time: {0:.6f}s ({1} reps)'.format(avg_run_time,reps))
            return result
        return inner
    return timed

@dec_factory1(5)
def fib(n):
    return calc_fib_recurse(n)

print(fib(28))