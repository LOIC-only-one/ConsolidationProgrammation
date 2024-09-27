from pokemon import Pokemon

class PokemonSportif(Pokemon):

    def __init__(self, nom: str, poids: int, taille: int, nb_pattes: int, frequence_cardiaque: int) -> None:
        super().__init__(nom, poids, taille, nb_pattes)
        self.__frequence_cardiaque = frequence_cardiaque

    def __str__(self) -> str:
        return f"{super().__str__()} et sa fréquence cardiaque est de {self.__frequence_cardiaque} bpm"

    def vitesse(self) -> float:
        """
        Calcule la vitesse du pokemon sportif

        :return: float
        """
        return self.nb_pattes * self.taille * 3
    
if __name__ == "__main__":
    p = PokemonSportif("Pikachu", 6, 40, 4, 120)
    print(p)
    print(p.vitesse())