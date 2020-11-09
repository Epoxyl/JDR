from Game.Classes.Objet.Equipement.Equipement import Equipement


class Bottes(Equipement):
  bonus_defense = 0
  def __init__(self,nom,prix,description,durabilite,poids,bonus_defense):
    super().__init__(self,nom,prix,description,durabilite,poids)
    self.bonus_attaque=bonus_defense