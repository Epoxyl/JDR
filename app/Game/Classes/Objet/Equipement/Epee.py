from Game.Classes.Objet.Equipement.Equipement import Equipement


class Epee(Equipement):
  infos_attaque_epee = {"type": "FOR"}
  bonus_attaque=0

  def __init__(self,nom,prix,description,durabilite,poids,bonus_attaque):
    super().__init__(self,nom,prix,description,durabilite,poids)
    self.bonus_attaque=bonus_attaque

  def attaque_epee(Character, target):
    print("Coup d'épée en scred!")
