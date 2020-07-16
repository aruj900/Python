class Rectangle:
    
    def __init__(self,width,height):
        self._width = width
        self._height = height
    
    def area(self):
        return self._width * self._height
    
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self._width, self._height)
    
    def get_width(self):
        return self._width
    
    def set_width(self,width):
        if width <= 0:
            raise ValueError('Width must be positive')
        else:
            self._width = width
            
    def __str__(self):
        return self.to_string()
    
    def __repr__(self):
        return 'Rectangle({0}, {1}'.format(self._width, self._height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            
            return (self._width, self._height) == (other._width,self._height)
        else:
            return False
    
    def __lt__(self,other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10,20)
r2 = Rectangle(100,20)

print(r1 is not r2)

print(r1 == r2)

print(r1.area())

print(r1.perimeter())

print(str(r1))

print(r1 == 100)

print(r1 < r2)

print(r1.set_width(100))

print(r1.get_width())

print(r1)