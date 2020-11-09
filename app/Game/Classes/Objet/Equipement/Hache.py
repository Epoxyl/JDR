from Game.Classes.Objet.Equipement.Equipement import Equipement


class Hache(Equipement):
  infos_attaque_hache = {"type": "FOR"}
  bonus_attaque = 0

  def __init__(self,nom,prix,description,durabilite,poids,bonus_attaque):
    super().__init__(self,nom,prix,description,durabilite,poids)
    self.bonus_attaque=bonus_attaque

  def attaque_hache(Character, target):
    print("Coup de hache bien vener!")