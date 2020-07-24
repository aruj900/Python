# boolean can act as integers also

print(True + True)

print(bool(0))

print(bool(1))

# Everything except 0 will be True

print(bool(None))

a = [1,2,3]
if a:
    print(a[0])
else:
    print('Nothing to print')
    
# if a acts like bool(a)

a = 10
b = 0

if b and a/b > 2:
    print("a is atleast twice b")


# to check in string

print([] or [0])

#X or Y if x is truly, return x ,, otherwise evaluate Y and return it

# X and Y if x is falsy return x otherwise evatuate and return Y


print([] and [0])


a = 2
b = 0

print(b and a/b)

s1 = 'abc'
s2 = None

print((s1 and s1[0]) or '' )

print((s2 and s2[0]) or 'n/a' )


print(not 'abc')



