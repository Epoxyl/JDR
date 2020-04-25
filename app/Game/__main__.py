from Game.Classes.Gobelin import Gobelin
from Game.Classes.Personnage import Personnage

def main():
    """
    Main program
    :return:
    """
    print("start")

    gobelin1 = Gobelin()

    personnage = Personnage("elfe", "chasseur")

    gobelin1.attaque(personnage)