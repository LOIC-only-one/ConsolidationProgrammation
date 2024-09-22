from batiment import Batiment

class SuperMarche(Batiment):

    def __init__(self, nom: str, adresse: str, array_aliment: list = [], nb_etage: int = 0) -> None:
        super().__init__(nom, adresse, nb_etage)
        self.aliment = array_aliment

    def ajouter_aliment(self, aliment: str) -> str:
        if aliment not in self.aliment:
            self.aliment.append(aliment)
            return f"Le produit {aliment} a été ajouté."
        else:
            return f"Le produit {aliment} existe déjà."

    def remove_aliment(self, aliment: str) -> str:
        if aliment not in self.aliment:
            return f"Le produit {aliment} n'existe pas."
        else:
            self.aliment.remove(aliment)
            return f"Le produit {aliment} a été supprimé."

    def __str__(self) -> str:
        return f"Le supermarché {self.nom} est situé à l'adresse {self.adresse}, a {self.nb_etage} étage(s) et contient les aliments suivants : {', '.join(self.aliment)}."