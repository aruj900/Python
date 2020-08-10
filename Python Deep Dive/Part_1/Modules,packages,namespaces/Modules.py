import math

print(math.__name__)

print(math.__dict__)

f = math.__dict__['sqrt']

print(f(2))

import types

print(isinstance(math, types.ModuleType))

mod = types.ModuleType('test','This is a test module.')

from types import ModuleType

print(isinstance(mod, types.ModuleType))

print(mod.__dict__)

mod.hello = lambda : 'hello'

print(mod.hello())

from collections import namedtuple
mod.Point = namedtuple('Point','x y')

p1 = mod.Point(0,0)
p2 = mod.Point(1,1)

print(p1)

PT = getattr(mod,'Point')

print(PT(20,20))

