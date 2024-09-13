import math

class Point:
    """
    Créer un objet point à partir de deux coordonnées x et y
    """

    def __init__(self, x : float = 0.0, y : float = 0.0) -> None:
        self.__x = x
        self.__y = y

    def __str__(self) -> str:
        return f"Point: ({self.__x}, {self.__y})"

    def distanceCord(self, a:float, b:float) -> float:
        """
        Calcule la distance entre le point et l'origine

        :param self: Point
        :param x: float
        :param y: float

        :return: float
        """
        return math.sqrt((self.__x - a)**2 + (self.__y - b)**2)

    def distancePoint(self,point) -> float:
        """
        Calcule la distance entre deux points a l'aide d'un plan

        :param point: Point
        :return float

        """
        return math.sqrt((self.__x - point.__x)**2 + (self.__y - point.__y)**2)
    
    @property
    def get_x(self) -> float:
        return self.__x
    @get_x.setter
    def set_x(self, x: float) -> None:
        if isinstance(self,(int,float)):
            self.__x = x

    @property
    def get_y(self) -> float:
        return self.__y
    @get_y.setter
    def set_y(self, y: float) -> None:
        if isinstance(self,(int,float)):
            self.__y = y

def main():
    p1 = Point(1,1)
    p2 = Point(2,2)
    p = Point()

    print(p1)
    print(p2)
    print(p1.distanceCord(2,2))
    print(p1.distancePoint(p2))

if __name__ == "__main__":
    main()