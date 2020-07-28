a = 10

def my_func(n):
    c = n ** 2
    return c

def my_func(n):
    print('global a:', a)
    c = a ** n
    return c

my_func(2)


def my_func(n):
    a = 20
    c = a ** n
    return c

# a is local to the function global a is still 10
print(my_func(2))
print(a)


def my_func(n):
    global a
    a = 20
    c = a ** n
    return c

# a is global as we used global keyword
print(a)
print(my_func(2))
print(a)


def my_func():
    global var
    var = 'hello world'
    return 
my_func()
print(var)