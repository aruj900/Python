#how to use do in while

i = 1
while True:
    print(i)
    if i >=5:
        break
        print('something')
    else:
        i +=1
        
#example of infinite loop

min_length = 2


while True:
    name = input("Please enter your name: ")
    
    if len(name) >= min_length and name.isprintable() and name.isalpha():
        break
    
print("Hello, {0}".format(name))



l = [1,2,3]
val = 10

found = False
idx = 0
while idx < len(l):
    if l[idx] == val:
        found = True
        break
    idx += 1
if not found:
    l.append(val)
print(l)


