from Game.Classes.Objet.Equipement.Equipement import Equipement


class Poing(Equipement):
  infos_attaque_epee = {"type": "FOR"}
  bonus_attaque=0
  double_mains = True
  deDegats = 4

  def __init__(self, nom="Poing", prix=0, description="", durabilite=100, poids=10, bonus_attaque=0):
    self.bonus_attaque=bonus_attaque
    super().__init__(nom, prix, description, durabilite, poids, emplacement="MAIN")

  def defaultAttack(self, Character, target):
    print("Coup de poing en scred!")
    super().defaultAttack(Character, target)
