from Game.Classes.Actors.Actor import Actor
from Game.Utils.Manipulations import array_intersect, dict_merge


class Meuble(Actor):
  durabilite = 100
  default_actions = {
    "laisser": {
      "active": True
    },
    "détruire": {
      "active": False
    }
  }

  def getActions(self, type = "", name = "", only_names = False, with_function = False):

    ret = {}
    actions = dict_merge(self.default_actions, self.interactions_meuble)

    for action_name in actions.keys():
      action = actions[action_name]
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

  def detruire(self):
    if self.durabilite < 0:
      print("Vous l'avez détruit")
    else:
      print("Vous attaquez l'objet")