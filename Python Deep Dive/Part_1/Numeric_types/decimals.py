import decimal
from decimal import Decimal

t = Decimal('-3.13534')
print(t)

#local and global context

a = Decimal('0.12345')
b = Decimal('0.12345')
print(a+b)
with decimal.localcontext() as ctx:
    ctx.prec = 2
    c = a + b
    print('c within local context: {0}'.format(c))
print('c within local context: {0}'.format(c))

#decimal has fixed representations 

#not all operations are allowed, use tuples to create
import time
n = 100000
def run_float(n=1):
    a = 3.145
    for i in range(n):
        a * a
        
def run_decimal(n = 1):
    a = Decimal('3.1415')
    for i in range(n):
        a * a


start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ',end-start)

start = time.perf_counter()
run_float(n)
end = time.perf_counter()
print('float: ',end-start)

#decimal is slow to operate but you get accurate result



