class Polygon:
    __width = None
    __height = None

    def set_data(self,width,heigt):
        self.__width =  width
        self.__height= heigt
    
    def get_width(self):
        return self.__width
    def get_height(self):
        return self.__height
    
class Rectangle(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

class Square(Polygon):
    def area(self):
        return self.get_width() * self.get_height()

rectangle = Rectangle()
rectangle.set_data(10,20)
print('Area of the rectangle is', rectangle.area())