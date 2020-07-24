def my_func(a,b=1):
    "returns a*b"
    return a*b
help(my_func)

def my_func1(a:'annotation for a',b: 'annotation for b'= 1) -> 'something with a long annotation':
    """documentation"""
    print(a*b)
    
help(my_func1)

x = 3
y = 5
def my_func3(a:'some character') -> 'character a repeated ' + str(max(x,y)) + ' times' :
    return a* max(x,y)

help(my_func3)

x = 10
print(my_func3('a'))
help(my_func3)


 