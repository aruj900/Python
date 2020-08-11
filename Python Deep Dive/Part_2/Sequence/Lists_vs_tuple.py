from dis import dis
dis(compile('(1,2,3,"a")', 'string', 'eval'))



dis(compile('[1,2,3,"a"]', 'string', 'eval'))

dis(compile('(1,2,3,[10,20])', 'string', 'eval'))

#If we dont need mutable type use tuple as it is more efficient

l1 = [1,2,3,4,5]
t1 = (1,2,3,4,5)

l2 = list(l1)
print(id(l1) , id(l2))

t2 = tuple(t1)

print(id(t1), id(t2))

# For tuple python creates a deep copy and for list a shallow copy

###Storage 
import sys

t = tuple()
prev = sys.getsizeof(t)
for i in range(10):
    c = tuple(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta={delta}')

l = list()
prev = sys.getsizeof(l)
for i in range(10):
    c = list(range(i+1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta={delta}')
    