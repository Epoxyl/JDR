from Game.Classes.Monstre import Monstre
from Game.Classes.Personnage import Personnage
from Game.Classes.Objet.Equipement.Epee import Epee

def main():
    """
    Main program
    :return:
    """
    print("start")

    gobelin1 = Monstre("Errek", "Gobelin", "Homme")

    personnage = Personnage("Yohann", "Humain", "Magicien")

    epeeDebatard = Epee("Epee de batard")

    personnage.setEquipement(epeeDebatard)

    print(personnage.toString())

    personnage.action("sortBouleDeFeu", {"target": gobelin1})

    #gobelin1.attaque(personnage)