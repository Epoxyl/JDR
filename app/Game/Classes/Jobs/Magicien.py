from Classes.Jobs.Jobs import Job

class Magicien(Job):
  deVie = 6

  actions = [
    [0, "sortBouleDeFeu", "INT", True],
    [0, "creerPortail", "INT", True]
  ]

  infos_sortBouleDeFeu = {"type": "INT"}
  infos_creerPortail = {"type": "INT", "difficulté": 14}


  @staticmethod
  def sortBouleDeFeu(Character, target):
    print("boule de feu !")

  @staticmethod
  def creerPortail(Character):
    print("Portail créé")