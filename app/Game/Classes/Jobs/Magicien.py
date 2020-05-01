from Game.Classes.Jobs.Jobs import Job

class Magicien(Job):
  deVie = 6

  infos_sortBouleDeFeu = {"type": "INT"}
  infos_creerPortail = {"type": "INT", "difficulté": 14}

  def sortBouleDeFeu(Character, target):
    print("boule de feu !")

  def creerPortail(self):
    print("Portail créé")