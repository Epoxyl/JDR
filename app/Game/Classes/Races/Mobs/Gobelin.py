from Game.Classes.Races.Races import Race

class Gobelin(Race):
  nom = "Gobelin"
  initiative = 11
  actions_race = {
    "attaqueRapide": {
      "type": "FOR",
      "active": True,
      "use": ["combat"]
    }
  }

  @staticmethod
  def attaqueRapide(Character, target):
    print("AttaqueRapide !")