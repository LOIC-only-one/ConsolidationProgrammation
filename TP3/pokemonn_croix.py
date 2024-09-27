from pokemon import Pokemon


class PokemonCroisiere(Pokemon):

    def __init__(self, nom: str, poids: int, taille: int, nb_pattes: int, nb_nageoire: int) -> None:
        super().__init__(nom, poids, taille, nb_pattes = 0)
        self.__nb_nageoire = nb_nageoire

    def __str__(self) -> str:
        return f"{super().__str__()} et a {self.__nb_nageoire} nageoires"
    
    def vitesse(self) -> float:
        return ( self.poids / 25 * self.__nb_nageoire ) / 2
    
if __name__ == "__main__":
    p = PokemonCroisiere("Magicarpe", 6, 40, 2, 2)
    print(p)
    print(p.vitesse())