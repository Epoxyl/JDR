from Game.Classes.Jobs.Jobs import Job

class Magicien(Job):
  deVie = 6

  actions_job = {
    "sortBouleDeFeu" : {
      "type": "INT",
      "active": True,
      "use": ["combat", "bruler"],
      "difficulty": 14,
      "level": 0,
    },

    "lireDraconien": {
      "type": "INT",
      "active":True,
      "use": ["information"]
    },
    
    "creerPortail": {
      "type": "INT",
      "active": False,
      "use": [],
      "level": 0
    }
  }

  def __init__(self):
    super().__init__("Magicien")

  @staticmethod
  def lireDraconien(Character, msg):
    """
    Lire un message en draconien
    :param str msg:
    :return:
    """
    print(msg)

  @staticmethod
  def sortBouleDeFeu(Character, target):
    """
    Envoie une boule de feu sur l'ennemi
    :param Magicien Character:
    :param Entity target:
    :return:
    """

    print("boule de feu sur {} !".format(target.nom))
    target.takeDamage(15)
    print(target.vie)

  @staticmethod
  def creerPortail(Character):
    print("Portail créé")