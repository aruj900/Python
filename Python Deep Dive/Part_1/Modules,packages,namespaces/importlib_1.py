import sys

mod_name = 'math'

#import mod_name

import importlib

print(importlib.import_module(mod_name))

math2 = importlib.import_module(mod_name)

print('math2' in globals())

print(math2.sqrt(2))


