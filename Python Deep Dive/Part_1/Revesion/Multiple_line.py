#implicit line continuation
a = [1 #item 1 
     ,2]
print(a)

d = {'key1': 1 #value 1
     ,'key2': 2 #value 2
}

print(d)
a= 0
b = 0
def func(a #first value
         ,b #second value
         ):
    a = 10
    b = 20
    '''aadasdasdasda
    '''
    return [a,b]

print(func(a,b))


#Explicit multiline

a = 10
b = 20
c = 30

if a > 5 \
    and  b > 10 \
        and c > 20:
            print('yes')
            

#Multiline string

n = '''This is a 
        string
            with multiple line'''
print(n)



