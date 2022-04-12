class Polygon:
    __width = None
    __height = None

    def set_data(self, width, height):
        self.__width = width
        self.__height = height

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


shape = Rectangle()

shape.set_data(20,10)
print(shape.area())

