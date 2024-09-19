class Personnage:
    """
    Permet de créer un objet personnage
    @method __init__ : Constructeur de la classe
    @method __str__ : Affichage de l'objet
    @method attaque(AutrePersonnage : Personnage) : str
    @method combat(AutrePersonnage : Personnage) : str
    @method soigne(AutrePersonnage : Personnage) : str
    """

    def __init__(self, pseudo : str, niveau : int = 1, nb_vie : int = 1, initiative : int = 1) -> None:
        """
        Constructeur de la classe Personnage
        :param pseudo
        :type str
        :param niveau
        :type int
        :param nb_vie
        :type int
        :param initiative
        :type int
        """
    
        self.pseudo = pseudo
        self.niveau = niveau
        self.nb_vie = nb_vie
        self.initiative = initiative
        
    def __str__(self) -> str:
        """
        Methode de traitement de chaine de caractère
        """
        return f"Le personnage {self.pseudo} a {self.nb_vie} vie(s), il est de niveau {self.niveau}, et a une initiative de {self.initiative} !"
        
    def attaque(self, autre_personnage) -> str:
        """
        Méthode pour attaquer un autre personnage.
        :param autre_personnage: L'autre personnage à attaquer
        :type autre_personnage: Personnage
        :return: Résultat de l'attaque
        :rtype: str
        """
        result = ""
        if self.initiative > autre_personnage.initiative:
            autre_personnage.nb_vie -= self.niveau
            result += f"{self.pseudo} attaque {autre_personnage.pseudo} et lui inflige 1 dégât.\n"
            if autre_personnage.nb_vie > 0:
                self.nb_vie -= 1
                result += f"{autre_personnage.pseudo} contre-attaque et inflige 1 dégât à {self.pseudo}.\n"
        elif self.initiative < autre_personnage.initiative:
            self.nb_vie -= autre_personnage.niveau
            result += f"{autre_personnage.pseudo} attaque {self.pseudo} et lui inflige 1 dégât.\n"
            if self.nb_vie > 0:
                autre_personnage.nb_vie -= self.niveau
                result += f"{self.pseudo} contre-attaque et inflige 1 dégât à {autre_personnage.pseudo}.\n"
        else:
            self.nb_vie -= autre_personnage.niveau
            autre_personnage.nb_vie -= self.niveau
            result += f"{self.pseudo} et {autre_personnage.pseudo} attaquent en même temps et s'infligent respectivement 1 dégât.\n"

        if self.nb_vie <= 0:
            result += f"{self.pseudo} est mort.\n"
        if autre_personnage.nb_vie <= 0:
            result += f"{autre_personnage.pseudo} est mort.\n"
        
        return result

    def combat(self, autre_personnage) -> str:
        """
        Réalise un combat entre deux personnages
        :param autre_personnage: L'autre personnage à combattre
        :type autre_personnage: Personnage
        """

        while self.nb_vie > 0 and autre_personnage.nb_vie > 0:
            self.attaque(autre_personnage)

            if self.nb_vie == 0:
                return f"{self.pseudo} a perdu le combat contre {autre_personnage.pseudo}."
            else:
                return f"{autre_personnage.pseudo} a perdu le combat contre {self.pseudo}."

    def soigne(self, autre_personnage) -> str:
        pass

    ## Définition des propriétés
    @property
    def initiative(self) -> int:
        return self.__initiative
    @initiative.setter
    def initiative(self, value : int) -> None:
        if isinstance(value, int):
            self.__initiative = value

def main():
    p1 = Personnage("Master", niveau=5, nb_vie=20, initiative=3)
    p2 = Personnage("Slave", niveau=4, nb_vie=18, initiative=3)
    print(p1)
    print(p2)
    print(p1.attaque(p2))
    print(p2.attaque(p1))
    print(p1)
    print(p2)

    p3 = Personnage("Master", niveau=5, nb_vie=20, initiative=3)
    p4 = Personnage("Slave", niveau=4, nb_vie=18, initiative=3)
    print(p3)
    print(p4)
    print(p3.combat(p4))

if __name__ == "__main__":
    main()