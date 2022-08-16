class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):

        if (type(x) == int) or (type(x) == float):     
             self.__x = x
        
            

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        print("y", y)
        if (type(y) == int) or (type(y) == float):
             self.__y = y


point = Point (5, 10)
print(point.x)
print(point.y)