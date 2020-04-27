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

    print(personnage.setEquipement(epeeDebatard))

    epee2 = Epee("Epee de la rue")
    print(personnage.setEquipement(deux_mains=True, equipement=epee2))
    epee3 = Epee("Epee de la mort")
    print(personnage.setEquipement(emplacement_voulu="MAIN2", equipement=epee3))

    print(personnage.toString())

    personnage.action("sortBouleDeFeu", {"target": gobelin1})

    #gobelin1.attaque(personnage)