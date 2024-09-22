class Batiment:

    def __init__(self, nom :str, adresse :str, nb_etage :int = 0) -> None:
        """
        Initialise un nouveau batiment avec un nom, une adresse et un nombre d'étages.

        :param nom: Le nom du batiment.
        :type nom: str
        :param adresse: L'adresse du batiment.
        :type adresse: str
        :param nb_etage: Le nombre d'étages du batiment.
        :type nb_etage: int
        """
        self.nom = nom
        self.adresse = adresse
        self.nb_etage = nb_etage

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de caractères du batiment.

        :return: Une chaîne de caractères décrivant le batiment.
        :rtype: str
        """
        return f"Le batiment {self.nom} est situé à l'adresse {self.adresse} et a {self.nb_etage} étage(s)."
    
    def add_etage(self,nb_etage):
        self.nb_etage += nb_etage
        return f"Le batiment {self.nom} a maintenant {self.nb_etage} étage(s)."
    
    def remove_etage(self,nb_etage):
        self.nb_etage -= nb_etage
        return f"Le batiment {self.nom} a maintenant {self.nb_etage} étage(s)."
    
    