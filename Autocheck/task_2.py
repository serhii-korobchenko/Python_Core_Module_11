class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @ property
    def x (self):
        print("property")
        return self.__x

    @x.setter
    def x(self, new_value_x):
        print('x.setter')
        self.__x = new_value_x + 5

    @ property
    def y (self):
        print("property")
        return self.__y

    @y.setter
    def y(self, new_value_y):
        print('y.setter')
        self.__y = new_value_y + 5

point = Point (5, 10)
print(point.x)
print(point.y)
