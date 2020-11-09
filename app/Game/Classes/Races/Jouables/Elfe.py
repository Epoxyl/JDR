from Game.Classes.Races.Races import Race

class Elfe(Race):
  nom = "Elfe"
  actions_race = {
    "tirArc": {
      "type": "FOR",
      "active": True,
      "use": ["combat"]
    }
  }

  def tirArc(Character, target):
    print(target)
    print("tirArc !")