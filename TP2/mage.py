from personnage import Personnage

class Mage(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        super().__init__(pseudo, niveau)
        self.nb_vie = niveau * 5 + 10
        self.initiative = niveau * 6 + 4
        self.mana = niveau * 5

    def degats(self) -> int:
        if self.mana >= 4:
            self.mana -= 4
            return self.niveau + 3
        else:
            return self.niveau