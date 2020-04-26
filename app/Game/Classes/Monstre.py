from Game.Classes.Entite import Entite

class Monstre(Entite):
  life = 0
  equipement = {
  }

  def __init__(self):
    print("I am born !")