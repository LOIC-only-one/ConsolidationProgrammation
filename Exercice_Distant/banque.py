from batiment import Batiment

class Banque(Batiment):
    def __init__(self, nom: str, adresse: str, nb_etage: int = 1, nb_coffre: int = 0) -> None:
        """
        Initialise une nouvelle banque avec un nom, une adresse, un nombre d'étages et un nombre de coffres.

        :param nom: Le nom de la banque.
        :type nom: str
        :param adresse: L'adresse de la banque.
        :type adresse: str
        :param nb_etage: Le nombre d'étages de la banque.
        :type nb_etage: int
        :param nb_coffre: Le nombre de coffres de la banque.
        :type nb_coffre: int
        """
        super().__init__(nom, adresse, nb_etage)
        self.nb_coffre = nb_coffre

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de caractères de la banque.

        :return: Une chaîne de caractères décrivant la banque.
        :rtype: str
        """
        return f"Banque {self.nom}, Adresse: {self.adresse}, Nombre d'étages: {self.nb_etage}, Nombre de coffres: {self.nb_coffre}"
    