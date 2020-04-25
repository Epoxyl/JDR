from Game.Classes.Monstre import Monstre

class Gobelin(Monstre):

  def __init__(self):
    self.life = 40
    print("gobelin Born with {}!".format(self.life))
    super().__init__()
