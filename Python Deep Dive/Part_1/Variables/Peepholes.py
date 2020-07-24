def my_func():
    a = 24*60
    b = (1,2) * 5
    c = 'abc' * 3
    d = 'ab' * 11
    e = 'the quick brown fox' * 5
    f = ['a','b']*3

print(my_func.__code__.co_consts)

def my_func1(e):
    if e in [1,2,3]:
        pass

print(my_func1.__code__.co_consts)

#Use sets as they are faster frozensets

import string
import time

string.ascii_letters
char_list  = list(string.ascii_letters)
char_tuple  = tuple(string.ascii_letters)
char_set = set(string.ascii_letters)
print(char_list)
print(char_tuple)
print(char_set)


def membership_test(n,container):
    for i in range(n):
        if 'z' in container:
            pass

start = time.perf_counter()
membership_test(10000000,char_list)
end = time.perf_counter()
print('list: ',end-start)

start = time.perf_counter()
membership_test(10000000,char_tuple)
end = time.perf_counter()
print('list: ',end-start)

start = time.perf_counter()
membership_test(10000000,char_set)
end = time.perf_counter()
print('list: ',end-start)

