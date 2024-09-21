from personnage import Personnage

class Guerrier(Personnage):
    def __init__(self, pseudo: str, niveau: int = 1) -> None:
        super().__init__(pseudo, niveau)
        self.nb_vie = niveau * 8 + 4
        self.initiative = niveau * 4 + 6

    def degats(self) -> int:
        return self.niveau * 2
