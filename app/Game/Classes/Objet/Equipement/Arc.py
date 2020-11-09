from Classes.Objet.Equipement.Equipement import Equipement


class Arc(Equipement):
  infos_tir_fleche = {"type": "DEX"}
  bonus_porte = 0

  def __init__(self, nom, prix, description, durabilite, poids, bonus_porte):
    super().__init__(self, nom, prix, description, durabilite, poids)
    self.bonus_porte= bonus_porte

  def tir_fleche(Character, target):
    print("Tir de fleche bien senti!")