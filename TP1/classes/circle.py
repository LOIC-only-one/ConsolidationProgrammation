from point import Point
import math

class Circle():
    """
    Créer un objet Circle
    """

    def __init__(self, rayon: float, point: Point = None) -> None:
        self.rayon = rayon
        self.point = point
    
    def CalculDiametre(self) -> float:
        """
        Calcule le diametre du cercle

        :param self: Circle
        :return: float
        """
        return 2 * self.rayon

    def CalculPerimetre(self) -> float:
        """
        Calcule le perimetre d'un cercle
        
        :param self: Circle
        :return: float
        """
        return 2 * math.pi * self.rayon
    
    def CalculSurface(self) -> float:
        """
        Calcule la surface d'un cercle

        :param self: Circle
        :return: float
        """
        return math.pi * self.rayon**2
    
    def SiAppartient(self, x: float, y: float) -> bool:
        """
        Vérifie si un point (x, y) appartient au cercle

        :param self: Circle
        :param x: float
        :param y: float
        :return: bool
        """    
        dx = x - self.point.get_x
        dy = y - self.point.get_y
        if math.sqrt(dx**2 + dy**2) <= self.rayon:
            return True

    def SiPointAppartient(self,other : Point) -> bool:
        """
        Vérifie si un point appartient au cercle

        :param self: Circle
        :param other: Point
        :return: bool
        """
        dx = other.get_x - self.point.get_x
        dy = other.get_y - self.point.get_y
        if math.sqrt(dx**2 + dy**2) <= self.rayon:
            return True
        
    @property
    def get_rayon(self) -> float:
        return self.rayon
    @get_rayon.setter
    def set_rayon(self, rayon: float) -> None:
        self.rayon = rayon
    

def main():
    p1 = Point(1, 1)
    c1 = Circle(5, Point(0, 0))
    print(c1.CalculDiametre())
    print(c1.CalculPerimetre())
    print(c1.CalculSurface())
    print(c1.SiAppartient(1, 1))
    print(c1.SiPointAppartient(p1))


if __name__ == "__main__":
    main()