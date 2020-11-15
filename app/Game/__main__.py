from Game.Controller.Server import Server
from Game.Utils.Session import Session


def main():
    """
    Main program
    :return:
    """

    # gobelin1 = Monstre("Errek", "Gobelin", "Homme")
    # gobelin1.initiative = 13
    #
    # personnage = Personnage("Yohann", "Humain", "Magicien")
    # personnage2 = Personnage("2", "Elfe", "Guerrier")
    # personnage3 = Personnage("3", "Humain", "Magicien")
    #
    # troupeAventuriers = [personnage, personnage2, personnage3]
    # ennemis = [gobelin1]
    #
    # combat = Combat([troupeAventuriers, ennemis])
    #
    # personnage.action("sortBouleDeFeu", gobelin1)
    # print(gobelin1.vie)
    # print(personnage.getActions(only_names=True, type="combat"))
    #combat.combat()


    server = Server()
    Session.set("Server", server)

    server.launchLevel()
    #chaise = Chaise([2,2])
    #chaise.inetraction(personnage)

    #scene = Chambre(7,20)

    #scene.description()

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