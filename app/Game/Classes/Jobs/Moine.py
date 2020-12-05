from Game.Classes.Jobs.Jobs import Job


class Moine(Job):
  deVie = 7

  actions_job = {
  }

  def __init__(self):
    super().__init__("Moine")