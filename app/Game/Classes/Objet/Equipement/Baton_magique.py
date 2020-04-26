class Baton_magique(Equipement):

  bonus_magie = 0

  def __init__(self,nom,prix,description,durabilite,poids,bonus_magie):
    Equipement.__init__(self,nom,prix,description,durabilite,poids)
    self.bonus_attaque=bonus_magie
