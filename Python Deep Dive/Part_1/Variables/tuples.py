#list dict are mutable

# tuple are immutable but instance inside them can change


a = [1,2]

b = [4,5]

t = (a,b)

a.append(3)
b.append(6)

print(t)


# String are immutable

def process(s):
    s = s + 'world'
    return s

my_var ='hello'

print(process(my_var))

#when we call process s will be saved at new memory address since strings are immutable

def process(s):
    print('Initial s # = {0}'.format(id(s)))
    s = s + ' world'
    print('Final s # = {0}'.format(id(s)))

my_var = 'hello'

print(process(my_var))

#Shared Reference

a = [1,2,3]
b = a

b.append(100)

print(a)