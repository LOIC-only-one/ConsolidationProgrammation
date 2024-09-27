from point import Point
import math
class TriangleRect:
    """
    Créer un triangle rectangle
    """

    def __init__(self,l1:float,l2:float,point=Point(0,0)) -> None:
        try:
            self.__l1 = l1
            self.__l2 = l2
        except TypeError:
            return "Probleme avec les longueurs"

    def __str__(self) -> str:
        return f"Triangle rectangle: ({self.__l1}, {self.__l2})"
    
    def CalculHypothenuse(self) -> float:
        """
        Calcule l'hypothenuse du triangle rectangle

        :param self: TriangleRect
        :return: float
        """
        return math.sqrt(self.__l1**2 + self.__l2**2)
    
    def CalulPerimetre(self) -> float:
        """
        Calcule le périmètre du triangle rectangle

        :param self: TriangleRect
        :return: float
        """
        return self.__l1 + self.__l2 + self.CalculHypothenuse()
    
if __name__ == "__main__":
    t1 = TriangleRect(3,4)
    print(t1)
    print(t1.CalculHypothenuse())
    print(t1.CalulPerimetre())