import random

class Job():
  rang = 0
  deVie = 0

  def getVie(self):
    vie = 0
    if self.deVie:
      vie = random.randint(1, self.deVie)
    return random.randint(1, self.deVie) if self.deVie else False