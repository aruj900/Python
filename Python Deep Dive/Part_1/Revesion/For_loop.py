i = 0
while i < 5:
    print(i)
    i += 1
i = None


#These two loops are very different range uses iterable 
for i in range(5):
    print(i)

# String, tuple and list are also iterable

# we can also break a for loop

for i in range(5):
    if i == 3:
        break
    print(i)

# else can also be used

for i in range(1,5):
    print(i)
    if i % 7 == 0:
        print('multiple of 7 found')
        break
else:
    print("no multiple of 7 in the range")

# else will trigger when we never hit break statement

# we can also use try except

for i in range(5):
    print("----------")
    try:
        10 /(i-3)
    except ZeroDivisionError:
        print("divided by zero")
        continue
    finally:
        print("always run")
    print(i)

s = "hello"
for c in s:
    print(c)

for i,c in enumerate(s):
    print(i,c)