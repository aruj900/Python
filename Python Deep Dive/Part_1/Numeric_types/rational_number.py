from fractions import Fraction
a = Fraction(1,2)
print(a)

import math
b = Fraction(math.pi)
print(b)

print(format(0.1,'.15f'))

x = 0.1 + 0.1 + 0.1
y = 0.3

print(x == y) 

#0.1 is not exact in base 2 binary thats why
from math import isclose
print(isclose(x,y))

print(round(1.88889,3))

