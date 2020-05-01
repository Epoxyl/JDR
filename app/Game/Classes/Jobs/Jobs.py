import random

class Job():
  rang = 0
  deVie = 0
  actions = {}

  def getFunctions(self):
    ret = []
    for i in range(len(self.actions)):
      if self.actions[i][3]:
        ret.append(self.actions[i])
    return ret

  def getVie(self):
    vie = 0
    if self.deVie:
      vie = random.randint(1, self.deVie)
    return random.randint(1, self.deVie) if self.deVie else False

  def __str__(self):
    msg = str(self.__class__.__name__)
    return msg