from pokemon import Pokemon

class PokemonMer(Pokemon):

    def __init__(self, nom: str, poids: int, taille: int, nb_nageoire : int) -> None:
        super().__init__(nom, poids, taille, nb_pattes=0)
        self.__nb_nageoire = nb_nageoire

    def __str__(self) -> str:
        return f"{super().__str__()} et a {self.__nb_nageoire} nageoires"
    
    def vitesse(self) -> float:
        return ( self.poids / 25 ) * self.__nb_nageoire
    
if __name__ == "__main__":
    p = PokemonMer("Magicarpe", 6, 40, 2)
    print(p)
    print(p.vitesse())