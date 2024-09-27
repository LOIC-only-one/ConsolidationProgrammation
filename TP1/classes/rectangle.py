from point import Point

class Rectangle:
    """
    Créer un objet Rectangle
    """

    def __init__(self, para_long_x: float = 1, para_hauteur_y: float = 1, point: Point = None, point_haut_droit: Point = None) -> None:
        """
        Initialise un rectangle avec ses dimensions et ses points

        :param para_long_x: Longueur du rectangle
        :param para_hauteur_y: Hauteur du rectangle
        :param point: Point bas gauche du rectangle
        :param point_haut_droit: Optionnellement, point haut droit du rectangle
        """
        try:
            if point_haut_droit is not None:
                self.point = point
                self.para_long_x = point_haut_droit.get_x - point.get_x
                self.para_hauteur_y = point_haut_droit.get_y - point.get_y
            else:
                if point is None:
                    self.point = Point(0, 0)
                else:
                    self.point = point
                self.para_long_x = para_long_x
                self.para_hauteur_y = para_hauteur_y
        except TypeError:
            return "Probleme avec les dimensions ou les points"
        
    def Surface(self) -> float:
        """
        Calcule la surface d'un rectangle

        :return: La surface du rectangle
        """
        surface = self.para_long_x * self.para_hauteur_y
        return surface

    def Perimetre(self) -> float:
        """
        Calcule le périmètre du rectangle

        :return: Le périmètre du rectangle
        """
        perimetre = 2 * (self.para_long_x + self.para_hauteur_y)
        return perimetre

    def PointBas(self) -> Point:
        """
        Renvoie le point bas gauche du rectangle

        :return: Le point bas gauche
        """
        return self.point

    def PointBasDroit(self) -> Point:
        """
        Renvoie le point bas droit du rectangle

        :return: Le point bas droit
        """
        point_bas_droit = Point(self.point.get_x + self.para_long_x, self.point.get_y)
        return point_bas_droit

    def PointHautGauche(self) -> Point:
        """
        Renvoie le point haut gauche du rectangle

        :return: Le point haut gauche
        """
        point_haut_gauche = Point(self.point.get_x, self.point.get_y + self.para_hauteur_y)
        return point_haut_gauche

    def PointHautDroit(self) -> Point:
        """
        Renvoie le point haut droit du rectangle

        :return: Le point haut droit
        """
        point_haut_droit = Point(self.point.get_x + self.para_long_x, self.point.get_y + self.para_hauteur_y)
        return point_haut_droit

    def SiAppartient(self, x: float, y: float) -> bool:
        """
        Vérifie si un point (x, y) appartient au rectangle

        :param x: Coordonnée x du point
        :param y: Coordonnée y du point
        :return: True si le point est dans le rectangle, False sinon
        """
        if (self.point.get_x <= x <= self.point.get_x + self.para_long_x and
            self.point.get_y <= y <= self.point.get_y + self.para_hauteur_y):
            return True
        else:
            return False

if __name__ == "__main__":
    r = Rectangle(2, 3, Point(0, 0))
    print("Surface:", r.Surface())
    print("Périmètre:", r.Perimetre())
    print("Point bas gauche:", r.PointBas())
    print("Point bas droit:", r.PointBasDroit())
    print("Point haut gauche:", r.PointHautGauche())
    print("Point haut droit:", r.PointHautDroit())
    print("Le point (1, 1) appartient-il au rectangle ?", r.SiAppartient(1, 1))
    print("Le point (3, 4) appartient-il au rectangle ?", r.SiAppartient(3, 4))
