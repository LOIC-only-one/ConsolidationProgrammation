class Pokemon:

    def __init__(self, nom: str, poids: int, taille: int, nb_pattes: int) -> None:
        self.__nom = nom
        self.__poids = poids
        self.__taille = taille
        self.__nb_pattes = nb_pattes

    @property
    def nom(self) -> str:
        return self.__nom

    @nom.setter
    def nom(self, nom: str) -> None:
        self.__nom = nom

    @property
    def poids(self) -> int:
        return self.__poids

    @poids.setter
    def poids(self, poids: int) -> None:
        self.__poids = poids

    @property
    def taille(self) -> int:
        return self.__taille

    @taille.setter
    def taille(self, taille: int) -> None:
        self.__taille = taille

    @property
    def nb_pattes(self) -> int:
        return self.__nb_pattes

    @nb_pattes.setter
    def nb_pattes(self, nb_pattes: int) -> None:
        self.__nb_pattes = nb_pattes

    def __str__(self) -> str:
        return f"Pokemon: {self.__nom}, {self.__poids} kg, {self.__taille} cm, {self.__nb_pattes} pattes"