def inc(x):
    return x + 1

def test__inc():
    assert inc(3) == 4
    assert inc(2) == 3
    assert inc(1) == 2

if __name__ == "__main__":
    test__inc()
    print("Tous les tests passent")
