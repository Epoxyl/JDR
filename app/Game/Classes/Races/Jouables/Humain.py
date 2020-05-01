from Game.Classes.Races.Races import Race

class Humain(Race):
  actions = [
    [0, "attaqueRapide", "FOR", True]
  ]

  def attaqueRapide(Character, target):
    print(target)
    print("AttaqueRapide !")