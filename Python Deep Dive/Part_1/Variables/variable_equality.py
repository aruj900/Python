a = 10
b = 10.0

print(id(a))
print(id(b))
print(a is b)

# is refers to memory 

a = 10 + 0j
b = 10

print(a is b)
print(a == b)

def cube(a):
    return a**3

def square(a):
    return a**2

def select_function(id):
    if id == 1:
        return square
    else:
        return cube
    
f = select_function(1)(3)

print(f)

