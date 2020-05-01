from Game.Classes.Races.Races import Race

class Gobelin(Race):
  initiative = 11
  actions = [
    [0, "attaqueRapide", "FOR", True, ]
  ]

  @staticmethod
  def attaqueRapide(Character, target):
    print("AttaqueRapide !")