class Point:

    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y
    
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x_setter(self, x: float):
        if isinstance(x, (int, float)):
            self.__x = x

if __name__ == "__main__":
    point = Point(3, 3)
    print(point.x)
    
    point.x_setter = 4
    print(point.x)