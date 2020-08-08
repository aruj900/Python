class Point3D:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
from collections import namedtuple

Point2D = namedtuple('Point2D',['x','y'])

pt1 = Point2D(10,20)

print(pt1)

pt3d_1 = Point3D(10,20,30)

print(pt3d_1)


p2 = Point2D(x=10,y=20)
print(p2)

#we can equate namedtuple but not class


pt1 = Point2D(10,20)
pt2 = Point2D(10,20)

print(pt1 is pt2)

print(pt1 == pt2)

pt1 = Point3D(10,20,30)
pt2 = Point3D(10,20,30)

print(pt1 is pt2)

print(pt1 == pt2)

class Point3D:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y={self.y},z={self.z}'
    
    def __eq__(self,other):
        if isinstance(other, Point3D):
            return self.x == other.x and self.y == other.y and self.z == other.z
        else:
            return False
        
pt1 = Point3D(10,20,30)
pt2 = Point3D(10,20,30)

print(pt1)

print(pt1 is pt2)

print(pt1 == pt2)


def dot_product_3d(a,b):
    return a.x * b.x + a.y * b.y + a.z * b.z


pt1 = Point3D(1,2,3)
pt2 = Point3D(1,1,1)

print(dot_product_3d(pt1,pt2))

# Now using zip and list comprehension

a = (1,2)
b = (1,1)

print(sum(e[0]*e[1] for e in zip(a,b)))

# Now lets do with named_tuple

def dot_product(a,b):
    return sum(e[0]*e[1] for e in zip(a,b))

pt1 = Point2D(1,2)
pt2 = Point2D(1,1)

print(dot_product(pt1,pt2))


# Advantage is that this is more general unlike 3d point class 

Vector3D = namedtuple('Vector3D','x y z')

v1 = Vector3D(1,2,3)
v2 = Vector3D(1,1,1)

print(dot_product(v1,v2))

# We can acccess is as a class as well as tuple

Stock = namedtuple('Stock', '''symbol
                   year
                   month
                   day
                   open
                   high 
                   low
                   close''')

djia = Stock('DJIA', 2018, 1, 25, 26_313, 26_458, 26_260, 26_393)

print(djia)

# we can do unpacking
symbol,year , *_, close = djia

print(symbol,year)

# we can unpack and change the list and then make it into tuple again

*values, _ = djia

values.append(26_393)

djia = Stock(*values)

print(djia)

print(id(djia))

djia = djia._replace(year=2019)

print(id(djia))

#since tuples are immutatble the address is different


# we can extend the tuple 

StockExt = namedtuple('StockExt', Stock._fields + ('previous_close',))

print(StockExt._fields)

djia_ext = StockExt(*djia,1_000_000)

print(djia_ext)


from collections import namedtuple
Point2D = namedtuple('Point2D','x y')

print(Point2D.__doc__)

print(Point2D.x.__doc__)

# we can change the docstrings

Point2D.__doc__ = '2D Coordinates'

print(Point2D.__doc__)


Vector2D = namedtuple('Vector2D','x1 y1 x2 y2 origin_x origin_y')

v1 = Vector2D(0,0,10,10,0,0)

# Prototyping for default values

vector_zero= Vector2D(0,0,0,0,0,0)

v2 = vector_zero._replace(x1=10,y1=10,x2=20,y2=20)

print(v2)

#we can also use __new__.__default__


Vector2D.__new__.__defaults__ = (-10,-10)

v1 = Vector2D(10,10,20,20)

print(v1)