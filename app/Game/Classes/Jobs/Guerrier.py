from Game.Classes.Jobs.Jobs import Job

class Guerrier(Job):
  deVie = 8

  actions = [
    (0, "taillade", "FOR", True),
  ]

  @staticmethod
  def taillade(Character, target):
    print("taillade à l'épée")