from banque import Banque
from batiment import Batiment
from supermarche import SuperMarche

if __name__ == "__main__":
    batiment = Batiment("Mairie", "1 rue de la mairie")
    print(batiment)
    print(batiment.add_etage(2))
    print(batiment.remove_etage(1))
    
    banque = Banque("Banque", "1 rue de la banque", 2, 10)
    print(banque)
    
    supermarche = SuperMarche("Supermarché", "1 rue du supermarché", ["Pomme", "Poire"], 1)
    print(supermarche)
    print(supermarche.ajouter_aliment("Banane"))
    print(supermarche.remove_aliment("Pomme"))
    print(supermarche.remove_aliment("Pomme"))

    banque.add_etage(2)
    print(banque)