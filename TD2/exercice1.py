def diviser(a, b):
    """
    Effectue la division de deux nombres réels.

    :param a: Le dividende.
    :type a: float
    :param b: Le diviseur.
    :type b: float
    :return: Le résultat de la division.
    :rtype: float
    """
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError("Les arguments doivent être des nombres réels (int ou float).")
        
        resultat = a / b
        return resultat

    except ZeroDivisionError:
        return "Erreur : Division par zéro."
    except TypeError as e:
        return f"Erreur de type : {e}"
    except Exception as e:
        return f"Une erreur inattendue s'est produite : {e}"

# Exemple d'utilisation
if __name__ == "__main__":
    # Cas de test
    print(diviser(10, 2))  # Devrait retourner 5.0
    print(diviser(10, 0))  # Devrait retourner "Erreur : Division par zéro."
    print(diviser(10, "a"))  # Devrait retourner "Erreur de type : Les arguments doivent être des nombres réels (int ou float)."
    print(diviser("a", 2))  # Devrait retourner "Erreur de type : Les arguments doivent être des nombres réels (int ou float)."
