def fib(n,memoize = {1:int(0),2:int(1)}):
    if n in memoize:
        return memoize[n]
    else:
        memoize[n] = fib(n-1,memoize) + fib(n-2,memoize)
        return memoize[n]
print(fib(11))