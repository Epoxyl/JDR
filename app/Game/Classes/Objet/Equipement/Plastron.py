from Classes.Objet.Equipement.Equipement import Equipement


class Plastron(Equipement):

  bonus_defense = 0

  def __init__(self,nom,prix,description,durabilite,poids,bonus_defense):
    Super().__init__(self,nom,prix,description,durabilite,poids)
    self.bonus_attaque=bonus_defense

    