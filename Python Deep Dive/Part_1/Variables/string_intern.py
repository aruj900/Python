import sys
a = sys.intern('the quick brown fox')
b = sys.intern('the quick brown fox')

#This will make sure is returns true and can help with memory optimization in NLP

print(a is b)

a1 = 'hello world'
b1 =  'hello world'

print(id(a1), id(b1))


def compare_interning(n):
    a = sys.intern('the quick brown fox'*200)
    b = sys.intern('the quick brown fox'*200)
    for i in range(n):
        if a is b:
            pass

def compare_equals(n):
    a = "a long string that is not intern"*200
    b = "a long string that is not intern"*200
    for i in range(n):
        if a == b:
            pass
        

import time

#start = time.perf_counter()
#compare_equals(10000000)
#end = time.perf_counter()
#print('equality', end-start)


start = time.perf_counter()
compare_interning(10000000)
end = time.perf_counter()
print('equality', end-start)

    