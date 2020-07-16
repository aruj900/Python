#we () to call otherwise it will be an object
def func(a:int,b:int):
    return a*b

print(func(2,4))

# you can still put string or list in first argument

def func_3():
    return func_4()

def func_4():
    return 'running func_4'

print(func_3())

#But remember you have to define func_4 before calling func_3

 #function ia an object
 
fn1 = lambda x: x**2
 
print(fn1(4))

