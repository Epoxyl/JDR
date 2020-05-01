
class Race():
  deVie = 0
  actions = {}

  def getFunctions(self):
    ret = []
    for i in range(len(self.actions)):
      if self.actions[i][3]:
        ret.append(self.actions[i])
    return ret

  def __str__(self):
    msg = str(self.__class__.__name__)
    return msg