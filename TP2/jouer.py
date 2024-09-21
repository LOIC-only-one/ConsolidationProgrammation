class Joueur:
    def __init__(self, pseudo: str, max_personnages: int) -> None:
        """
        Initialise un nouveau joueur avec un pseudo et un nombre maximum de personnages.

        :param pseudo: Le pseudo du joueur.
        :type pseudo: str
        :param max_personnages: Le nombre maximum de personnages que le joueur peut avoir.
        :type max_personnages: int
        """
        self.pseudo = pseudo
        self.max_personnages = max_personnages
        self.personnage_array = []

    def __str__(self) -> str:
        """
        Retourne une représentation sous forme de chaîne de caractères du joueur.

        :return: Une chaîne de caractères décrivant le joueur.
        :rtype: str
        """
        return f"Le joueur {self.pseudo} a {len(self.personnage_array)} personnage(s)."
    
    def ajouter_personnage(self, personnage) -> str:
        """
        Ajoute un personnage au joueur.

        :param personnage: Le personnage à ajouter.
        :type personnage: Personnage
        :return: Une chaîne de caractères décrivant le résultat de l'ajout.
        :rtype: str
        """
        if len(self.personnage_array) < self.max_personnages:
            self.personnage_array.append(personnage)
            return f"{personnage.pseudo} a été ajouté à la liste des personnages de {self.pseudo}."
        else:
            return f"{self.pseudo} ne peut pas ajouter plus de personnages."
        
    def get_personnage_id(self, numero : int) -> str:
        """
        Retourne un personnage du joueur.

        :param numero: Le numéro du personnage à retourner.
        :type numero: int
        :return: Une chaîne de caractères décrivant le personnage.
        :rtype: str
        """
        if self.personnage_array[numero]:
            return self.personnage_array[numero]
        
    def get_personnage_name(self,name :str) -> str:
        """
        Retourne un personnage du joueur.

        :param name: Le nom du personnage à retourner.
        :type name: str
        :return: Une chaîne de caractères décrivant le personnage.
        :rtype: str
        """
        for personnage in self.personnage_array:
            if personnage.pseudo == name:
                return personnage
        return f"Le personnage {name} n'existe pas."
    
    def get_personnage(self, personnage) ->str:
        """
        Retourne un personnage du joueur.

        :param personnage: Le personnage à retourner.
        :type personnage: Personnage
        :return: Une chaîne de caractères décrivant le personnage.
        :rtype: str
        """
        if personnage in self.personnage_array:
            return personnage
        else:
            return f"Le personnage {personnage.pseudo} n'existe pas."
        