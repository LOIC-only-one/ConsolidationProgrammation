def divide(a : float, b : float) -> float:
    """
    Cette fonction permet de deviser deux reels a et b
    
    :param a: float
    :param b: float
    :return: float

    """

    try:
        if isinstance(a, float) and isinstance(b, float):
            return a/b
        else:
            raise TypeError("a et b doivent etre des reels")
    except ZeroDivisionError:
        return "Impossible de diviser par zero"
