from Game.Classes.Monstre import Monstre
from Game.Classes.Personnage import Personnage

def main():
    """
    Main program
    :return:
    """
    print("start")

    gobelin1 = Monstre("Errek", "Gobelin", "Homme")

    personnage = Personnage("Yohann", "Humain", "Magicien")

    print(personnage.__str__());

    personnage.action("sortBouleDeFeu", {"target": gobelin1})

    #gobelin1.attaque(personnage)