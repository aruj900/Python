a = (1,2,3)
print(type(a))

# To create tuple we need ,

a = 100,

type(a)

a,b,c = [1,2,3]

print(a)

a,b = b,a # will swap the variables

# sets are not ordered

s = {'p', 'y', 't', 'h', 'o', 'n'}

print(s)

for e in s:
    print(e)


dict = {'a':1, 'b':2, 'c':3, 'd':4}

for a,b in dict.items():
    print('key={0}, value={1}')


a, *b = [-10,5,2,100]

print(a)
print(b)


l = [1,2,3,4,5,6]

a = l[0]

b = l[1:]

print(a)
print(b)

s = 'python'
a = s[0]
b = s[1:]

a , *b = s


l1 = [1,2,3]
s = 'abc'

print([*l1,*s])

s1 = {1,4,6}
s2 = {3,5,8}

s3 = {*s1,*s2}
print(s3)


# how to unpack dictonary

d1 = {'key1':1,'key2':2}
d2 = {'key3':3,'key4':4}

print({**d1,**d2})

#unpacking in functions

def funcl(a,b,*c):
    print(a)
    print(b)
    print(c)
    
print(funcl(10,20,1,2,3))


# Use case for short circuiting 
def avg(*args):
    count = len(args)
    total = sum(args)
    return count and total/count
    
print(avg(10,20))

print(avg())



def func1(a,b,c):
    print(a)
    print(b)
    print(c)
    
l = [10,20,30]

print(func1(*l))

# if you want to pass after * args argument than it must be keyword argument

# if you use keyword once then keep using


def func1(a,b, *args):
    print(a,b,args)

print(func1(1,2,3,4))


def func2(*args,d='a'):
    print(args,d)
    
print(func2(1,2,3, d ='a'))


def func(*,d):
    print(d)

print(func(d=100))

def func3(a,b,*,d):
    print(a,b,d)
    
print(func3(a,b,d=4))