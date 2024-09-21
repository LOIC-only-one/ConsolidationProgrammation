from mage import Mage
from guerrier import Guerrier

def main():
    guerrier = Guerrier("Conan", niveau=3)
    mage = Mage("Gandalf", niveau=2)

    print(guerrier.attaque(mage))

if __name__ == "__main__":
    main()
