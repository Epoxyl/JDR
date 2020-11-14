from Game.Utils.Manipulations import array_intersect
from abc import ABC, abstractmethod

class Race():
  deVie = 0
  actions_race = {}

  @classmethod
  def __init__(self, nom="Magicien"):
    self.nom = nom

  @classmethod
  def getActions(self, type = "", name = "", only_names = False, with_function = False):
    """
    Récupère les actions possibles suivant le type
    :param string type:
    :return:
    """
    # todo: optimiser pour une action

    ret = {}
    for action_name in self.actions_race.keys():
      action = self.actions_race[action_name]
      if not action["active"]:
        continue

      if (name and name != action_name) or (type and not array_intersect(type, action["use"])):
        continue

      if with_function:
        action_function = getattr(self, action_name)
        ret[action_name] = [self, action_function]
      elif only_names:
        ret[action_name] = action_name
      else:
        ret[action_name] = action

      if name:
        break
    return ret

  def __str__(self):
    msg = str(self.__class__.__name__)
    return msg