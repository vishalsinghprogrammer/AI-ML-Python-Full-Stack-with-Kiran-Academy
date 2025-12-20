from shapeEx import shape
class Rectangle(shape):
    def __init__(self,l,w):
        self.lenght=l
        self.width=w
    def area (self):
        return self.lenght*self.width
    def perimeter(self):
        return 2*(self.lenght+self.width)    
    
r1=Rectangle(100,50)
print(r1.area())
print(r1.perimeter())

        