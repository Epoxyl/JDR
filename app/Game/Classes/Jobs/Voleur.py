from Game.Classes.Jobs.Jobs import Job


class Voleur(Job):
  deVie = 7

  actions_job = {
    "backstab": {
      "type": "DEX",
      "active": True,
      "use": "combat",
      "difficulty": 12,
      "level": 0,
    },
    "crocheter": {
      "type": "DEX",
      "active": True,
      "use": ["ouvrir"],
      "difficulty": 14,
      "level": 0,
    },
  }

  def __init__(self):
    super().__init__("Voleur")
