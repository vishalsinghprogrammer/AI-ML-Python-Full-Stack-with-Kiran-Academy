from shapeEx import shape
class square(shape):
    def __init__(self,s):
        self.suare=s
    def area (self):
        return self.suare
    def perimeter(self):
        return 2*(self.suare)    
    
r1=square*2
print(r1.area(10))
print(r1.perimeter())