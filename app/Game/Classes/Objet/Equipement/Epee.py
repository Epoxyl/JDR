from Game.Classes.Objet.Equipement.Equipement import Equipement


class Epee(Equipement):
  infos_attaque_epee = {"type": "FOR"}
  bonus_attaque=0

  def __init__(self, nom="Epee", prix=0, description="", durabilite=100, poids=10, bonus_attaque=0):
    self.bonus_attaque=bonus_attaque
    super().__init__(nom, prix, description, durabilite, poids, "MAIN")  # __init__ toujours à la fin ;)

  def attaque_epee(Character, target):
    print("Coup d'épée en scred!")
