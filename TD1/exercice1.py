def max(a:float,b:float)-> float:
    if a > b:
        return a
    return b

def seuil(a:float, seuil:float = 10) -> bool:
    if seuil > a:
        return False
    return True

def maxArray(array:list[float]) -> float:
    
    max = 0
    for element in array:
        if element > max:
            max = element 
    pass
    return max


def main() -> None:
    print(max(1,2))
    print(seuil(11))
    print(maxArray([1,2,3]))


if __name__ == "__main__":
    main()