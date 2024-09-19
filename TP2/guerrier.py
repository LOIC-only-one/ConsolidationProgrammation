from personnage import Personnage

class Guerrier(Personnage):
    """
    On veut dans le constructeur pseudo & niveau
    On recupre pseudo, niveau, nb_vie, initiative
    """
    def __init__(self, pseudo, niveau=1) -> None:
        nb_vie = niveau * 8 + 4
        initiative = niveau * 4 + 6
        super().__init__(pseudo, niveau, nb_vie, initiative)
        self.arme = "Epée"

    def __str__(self) -> str:
        """
        Methode de traitement de chaine de caractère
        """
        return f"Le guerrier {self.pseudo} a {self.nb_vie} vie(s), il est de niveau {self.niveau}, et a une initiative de {self.initiative} ! Il est armé d'une {self.arme}."

def main():
    g1 = Guerrier("Conan", niveau=3)
    g2 = Guerrier("Thor", niveau=5)
    print(g1)
    print(g2)
    print(g1.attaque(g2))
    print(g2.attaque(g1))
    print(g1)
    print(g2)

if __name__ == "__main__":
    main()