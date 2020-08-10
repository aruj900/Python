import sys

for key in sorted(sys.modules.keys()):
    print(key)
    
print('cmath' in sys.modules)

print('cmath' in globals())

#If we import only exp from cmath still whole cmath package is loaded but only exp is included4
#  in namespace (global)
from cmath import exp

print('cmath' in globals())

print('cmath' is sys.modules)

#it takes almost same time



