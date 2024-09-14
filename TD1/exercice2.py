class Tasse:
    matière = "céramique"

    def __init__(self, couleur, contenance, marque):
        self.couleur = couleur
        self.contenance = contenance
        self.marque = marque

    def __str__(self):
        """
        Fonction de print d'un objet Tasse
        """
        return f"la tasse de matière {Tasse.matière}, de couleur {self.couleur} et de marque {self.marque} a une contenance de {self.contenance} ml"

    def definir_contenu(self, contenu):
        """
        Renvoi le contenu d'une tasse

        :param contenu
        :type float
        """        
        if isinstance(self,str):
            self.contenu = contenu

    def boire(self):
        """
        Supprime le contenu d'une tasse
        """
        del self.contenu