

def my_func(a,b):
    print(a,b)

x = 10
y = 2

print(my_func(x,y))    

# pointers x and y will now act as pointer to a and b

# If we have default values every value after that must be default

# if you use keyword argument then use all leywords argument

def my_func(a,b=20,c=30):
    print("a={0}, b={1}, c={2}".format(a,b,c))
    
print(my_func(10))