from Game.Utils.Manipulations import array_intersect
from abc import ABC, abstractmethod

import random

class Job(ABC):
  rang = 0
  deVie = 0
  actions_job = {}

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

    ret = []
    for action_name in self.actions_job.keys():
      action = self.actions_job[action_name]
      if not action["active"]:
        continue

      if (name and name != action_name) or (type and not array_intersect(type, action["use"])):
        continue

      if with_function and action_name:
        action_function = getattr(self, action_name)
        ret.append([action_name, self, action_function])
      elif only_names:
        ret.append(action_name)
      else:
        ret.append(action_name if only_names else {action_name: action})

      if name:
        break
    return ret

  def getVie(self):
    vie = 0
    if self.deVie:
      vie = random.randint(1, self.deVie)
    return random.randint(1, self.deVie) if self.deVie else False

  def __str__(self):
    msg = str(self.__class__.__name__)
    return msg