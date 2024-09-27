from pokemon import Pokemon
from pokemon_sportif import PokemonSportif
from pokemon_casaniers import PokemonCasanier
from pokemon_mers import PokemonMer
from pokemonn_croix import PokemonCroisiere

def main():
    # Question 3: Créer un ensemble de Pokémon de chacune des catégories
    p1 = PokemonCasanier("Bulbizarre", 6, 40, 4, 8)
    p2 = PokemonMer("Magicarpe", 6, 40, 2)
    p3 = PokemonCroisiere("Magicarpe", 6, 40, 2, 2)
    p4 = PokemonSportif("Pikachu", 6, 40, 4, 120)

    # Question 4: Définir un tableau de Pokémon avec les Pokémon définis à la question 3
    tableau_pokemons = [p1, p2, p3, p4]

    # Afficher les Pokémon en utilisant une boucle for sur le tableau
    for pokemon in tableau_pokemons:
        print(pokemon)
        print(pokemon.vitesse())

if __name__ == "__main__":
    main()