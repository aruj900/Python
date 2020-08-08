def outer1_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()

outer1_func()

def outer_func():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner:',x)
    inner()
    print('outer:',x)

outer_func()

#Just like global we need to use nonlocal to call upper level function
def outer2_func():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python'
        print('inner:',x)
    print('outer(before):',x)
    inner()
    print('outer(after):',x)

outer2_func()

def outer3_func():
    x = 'hello'
    def inner1():
        nonlocal x
        x = 'python'
        def inner2():
            nonlocal x
            x = 'monty'
        inner2()
    inner1()
    print(x)
    
outer3_func()
