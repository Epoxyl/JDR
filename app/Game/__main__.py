from Game.Classes.Gobelin import Gobelin

def main():
    """
    Main program
    :return:
    """
    print("start")

    gobelin1 = Gobelin()
    personnage = Personnage()

    gobelin1.attaque(personnage=personnage)