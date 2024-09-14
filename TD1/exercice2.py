class Tasse:
    matière = "céramique"

    def __init__(self, couleur, contenance, marque):
        self.__couleur = couleur
        self.__contenance = contenance
        self.__marque = marque

    def __str__(self):
        """
        Fonction de print d'un objet Tasse
        """
        return f"la tasse de matière {Tasse.matière}, de couleur {self.__couleur} et de marque {self.__marque} a une contenance de {self.__contenance} ml"

    def definir_contenu(self, contenu):
        """
        Renvoi le contenu d'une tasse

        :param contenu
        :type float
        """        
        if isinstance(contenu, str):
            self.__contenu = contenu

    def boire(self):
        """
        Supprime le contenu d'une tasse
        """
        del self.__contenu