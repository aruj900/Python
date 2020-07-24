f = lambda x: x**2
print(f(4))

f1 = lambda x, *args, y, **kwargs: (x,args,y,kwargs)

print(f1(1,'a','b',y=100,a=10,b=20))

def apply_func1(x,fn):
    return fn(x)

print(apply_func1(3,lambda x: x**2))

def apply_func(fn,*args,**kwargs):
    return fn(*args, **kwargs)

print(apply_func(lambda x: x**2,3))

print(apply_func(lambda x,y: x+y,1,2))

print(apply_func(lambda x, *, y: x+y,1,y=20))

print(apply_func(lambda *args: sum(args),1,2,3,4,5))

