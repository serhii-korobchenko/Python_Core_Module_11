class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @ property
    def x (self):
        return self.__x

    @x.setter
    def x(self, new_value_x):
        self.__x = new_value_x

    @ property
    def y (self):
        return self.__y

    @y.setter
    def y(self, new_value_y):
        self.__y = new_value_y

point = Point (5, 10)
print(point.x)
print(point.y)
