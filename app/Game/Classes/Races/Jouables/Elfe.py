from Classes.Races.Races import Race

class Elfe(Race):
  actions = [
    [0, "tirArc", "FOR", True]
  ]

  def tirArc(Character, target):
    print(target)
    print("tirArc !")