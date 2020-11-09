from Game.Classes.Jobs.Jobs import Job

class Guerrier(Job):
  deVie = 8

  actions_job = {
    "taillade" : {
      "type": "FOR",
      "active": True,
      "use": ["combat", "trancher"],
      "level": 0
    }
  }

  @staticmethod
  def taillade(Character, target):
    print("taillade à l'épée")