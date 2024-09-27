from pokemon import Pokemon

class PokemonCasanier(Pokemon):

    def __init__(self, nom, poids, taille, nb_pattes, nb_heures_tv):
        super().__init__(nom, poids, taille, nb_pattes)
        self.__nb_heures_tv = nb_heures_tv

    def __str__(self):
        return f"{super().__str__()} et regarde la télé {self.__nb_heures_tv} heures par jour"
    
    def vitesse(self):
        return self.nb_pattes * self.taille * 3
    

if __name__ == "__main__":
    p = PokemonCasanier("Bulbizarre", 6, 40, 4, 8)
    print(p)
    print(p.vitesse())