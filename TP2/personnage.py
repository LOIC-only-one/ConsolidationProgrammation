class Personnage:
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        """
        Initialise un nouveau personnage avec un pseudo et un niveau.

        :param pseudo: Le pseudo du personnage.
        :type pseudo: str
        :param niveau: Le niveau du personnage, par défaut 1.
        :type niveau: int
        """

        self.pseudo = pseudo
        self.niveau = niveau
        self.nb_vie = niveau
        self.initiative = niveau

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de caractères du personnage.

        :return: Une chaîne de caractères décrivant le personnage.
        :rtype: str
        """
        return f"Le personnage {self.pseudo} a {self.nb_vie} vie(s), il est de niveau {self.niveau}, et a une initiative de {self.initiative}."

    def degats(self) -> int:
        """
        Calcule les dégâts occasionnés par le personnage.

        :return: Les dégâts occasionnés par le personnage.
        :rtype: int
        """
        return self.niveau
    
    def attaque(self, autre_personnage) -> str:
        """
        Attaque un autre personnage et retourne le résultat de l'attaque.

        :param autre_personnage: Le personnage attaqué.
        :type autre_personnage: Personnage
        :return: Une chaîne de caractères décrivant le résultat de l'attaque.
        :rtype: str
        """
        result = ""
        if self.initiative > autre_personnage.initiative:
            degats = self.degats()
            autre_personnage.nb_vie -= degats
            result += f"{self.pseudo} attaque {autre_personnage.pseudo} et lui inflige {degats} dégâts.\n"
            if autre_personnage.nb_vie > 0:
                contre_degats = autre_personnage.degats()
                self.nb_vie -= contre_degats
                result += f"{autre_personnage.pseudo} contre-attaque et inflige {contre_degats} dégâts à {self.pseudo}.\n"
        elif self.initiative < autre_personnage.initiative:
            degats = autre_personnage.degats()
            self.nb_vie -= degats
            result += f"{autre_personnage.pseudo} attaque {self.pseudo} et lui inflige {degats} dégâts.\n"
            if self.nb_vie > 0:
                contre_degats = self.degats()
                autre_personnage.nb_vie -= contre_degats
                result += f"{self.pseudo} contre-attaque et inflige {contre_degats} dégâts à {autre_personnage.pseudo}.\n"
        else:
            degats = self.degats()
            autre_personnage.nb_vie -= degats
            self.nb_vie -= autre_personnage.degats()
            result += f"Les deux personnages ont la même initiative et s'attaquent en même temps.\n"

        result += f"Après l'attaque, {self.pseudo} a {self.nb_vie} vie(s) et {autre_personnage.pseudo} a {autre_personnage.nb_vie} vie(s).\n"
        return result

    def combat(self, autre_personnage) -> str:
        """
        Engage un combat avec un autre personnage jusqu'à ce que l'un des deux soit vaincu.

        :param autre_personnage: Le personnage avec lequel combattre.
        :type autre_personnage: Personnage
        :return: Une chaîne de caractères décrivant le résultat du combat.
        :rtype: str
        """
        result = ""
        while self.nb_vie > 0 and autre_personnage.nb_vie > 0:
            result += self.attaque(autre_personnage)
            if self.nb_vie <= 0:
                result += f"{self.pseudo} a perdu le combat contre {autre_personnage.pseudo}.\n"
                return result
            if autre_personnage.nb_vie <= 0:
                result += f"{autre_personnage.pseudo} a perdu le combat contre {self.pseudo}.\n"
                return result
        return result

    def soigne(self) -> str:
        """
        Soigne le personnage en lui restaurant ses points de vie à son niveau initial.

        :return: Une chaîne de caractères indiquant que le personnage est soigné.
        :rtype: str
        """
        self.nb_vie = self.niveau
        return f"{self.pseudo} est soigné et retrouve {self.nb_vie} points de vie."