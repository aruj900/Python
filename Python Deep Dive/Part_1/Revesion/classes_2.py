class Rectangle:
    
    def __init__(self,width,height):
        self.width = width
        self.height = height
        
    @property 
    def width(self):
        #print("get width")
        return self._width
    
    @width.setter
    def width(self,width):
        if width <= 0:
            raise ValueError('Width must be positive.')
        else:
            self._width = width
            
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self,height):
        if height <= 0:
            raise ValueError('Height must be positive.')
        else:
            self._height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def to_string(self):
        return 'Rectangle: width={0}, height={1}'.format(self.width, self.height)
     
            
    def __str__(self):
        return self.to_string()
    
    def __repr__(self):
        return 'Rectangle({0}, {1}'.format(self.width, self.height)
    
    def __eq__(self, other):
        if isinstance(other, Rectangle):
            
            return (self.width, self.height) == (other.width,self.height)
        else:
            return False
    
    def __lt__(self,other):
        if isinstance(other, Rectangle):
            return self.area() < other.area()
        else:
            return NotImplemented

r1 = Rectangle(10,20)
r2 = Rectangle(100,20)

r1.width = 10
print(r1.width)

