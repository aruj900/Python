from functools import partial

def my_func(a,b,c):
    print(a,b,c)
    
print(my_func(10,20,30))


def f(x,y):
    return my_func(10,x,y)

print(f(20,30))

f = lambda x,y: my_func(10,x,y)

print(f(100,200))

f1 = partial(my_func,10)

print(f1(20,30))

def my_func(a,b, *args, k1, k2, **kwargs):
    print(a,b,args,k1,k2,kwargs)
    
print(my_func(10,20,100,200, k1 = 'a', k2 = 'b', k3=1000, k4= 2000))


def f(x, *args, kw, **kwargs):
    return my_func(10,x,*args,k1='a',k2=kw,**kwargs)

print(f(20,100,200,kw='b',k3=1000,k4=2000))

f = partial(my_func, 10, k1='a')

print(f(20,100,200,k2='b',k3=1000,k4= 2000))


def pow(base,exponent):
    return base ** exponent

sq = partial(pow,exponent=2)

print(sq(10))

cu = partial(pow,exponent=3)

print(cu(10))

def my_func1(a,b):
    print(a,b)
    
a= [1,2]
a.append(3)
f = partial(my_func1,a)

print(f(100))


origin = (0,0)

l = [(1,1),(0,2),(-3,2),(0,0),(10,10)]

dist2 = lambda x,y: (x[0] - y[0])**2 + (x[1] - y[1])**2

print(dist2((1,1),origin))

f = partial(dist2,origin)

print(sorted(l,key=f))