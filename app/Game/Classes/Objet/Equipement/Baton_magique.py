from Game.Classes.Objet.Equipement.Equipement import Equipement


class Baton_magique(Equipement):

  bonus_magie = 0

  def __init__(self,nom,prix,description,durabilite,poids,bonus_magie):
    super().__init__(self,nom,prix,description,durabilite,poids)
    self.bonus_attaque=bonus_magie
