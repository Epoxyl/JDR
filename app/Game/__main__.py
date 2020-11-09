from Game.Classes.Monstre import Monstre
from Game.Classes.Personnage import Personnage
from Game.Classes.Objet.Equipement.Epee import Epee
from Game.Classes.Combat import Combat

def main():
    """
    Main program
    :return:
    """
    print("start")

    gobelin1 = Monstre("Errek", "Gobelin", "Homme")
    gobelin1.initiative = 13

    personnage = Personnage("Yohann", "Humain", "Magicien")
    personnage2 = Personnage("2", "Elfe", "Guerrier")
    personnage3 = Personnage("3", "Humain", "Magicien")

    troupeAventuriers = [personnage, personnage2, personnage3]
    ennemis = [gobelin1]

    combat = Combat([troupeAventuriers, ennemis])

    combat.combat()

    #epeeDebatard = Epee("Epee de batard")
#
    #print(personnage.setEquipement(epeeDebatard))
#
    #epee2 = Epee("Epee de la rue")
    #print(personnage.setEquipement(deux_mains=True, equipement=epee2))
    #epee3 = Epee("Epee de la mort")
    #print(personnage.setEquipement(emplacement_voulu="MAIN2", equipement=epee3))
#
    #print(personnage.toString())
#
    #personnage.action("sortBouleDeFeu", {"target": gobelin1})
#
    ##gobelin1.attaque(personnage)