from personnage import Personnage

class Mage(Personnage):

    def __init__(self, pseudo, niveau=1) -> None:
        nb_vie = niveau * 5 + 10
        initiative = niveau * 6 + 4
        mana = niveau * 5
        super().__init__(pseudo, niveau, nb_vie, initiative)
        self.mana = mana

    def __str__(self) -> str:
        """
        Methode de traitement de chaine de caractère
        """
        return f"Le mage {self.pseudo} a {self.nb_vie} vie(s), il est de niveau {self.niveau}, a une initiative de {self.initiative}, et possède {self.mana} points de mana."

def main():
    m1 = Mage("Gandalf", niveau=3)
    m2 = Mage("Merlin", niveau=5)
    print(m1)
    print(m2)

if __name__ == "__main__":
    main()