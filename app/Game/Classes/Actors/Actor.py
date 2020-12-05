from abc import ABC, abstractmethod

from Game.Utils.Logs import Log
from Game.Utils.Manipulations import RepresentsInt
from Game.Utils.Session import Session


class Actor(ABC):
  position = [0, 0]
  short_description_str = "Actor"
  description_str = "Actor"
  actor_object = None
  actions_possibles = {}
  actions = []

  def __init__(self, position):
    """
    :param Int[] position:
    """
    self.position = position

  def interaction(self, other=None, context=""):
    """

    :param Actor other:
    :return action:
    """
    Log.printlog("interaction entre {} et {}".format(other.short_description_str, self.short_description_str))
    msg = self.description_str + "\nQue voulez-vous faire ?"
    # other.setPosition(self.position)
    actions_propose = self.getActions(with_function=True)
    if (actions_propose):
      print(other)
      action_key = other.ask(msg, list(actions_propose.keys()), True)
      print(action_key)


  def ask(self, msg, choix=None, get_choice_str=False, get_object=False):
    """
    Affichage de question ainsi que les réponses disponibles au joueur
    :param string msg: Message/question à afficher
    :param choix:
    :return:
    """

    Session.get("User").askQuestion(self, msg, choix, get_choice_str, get_object)
    # if (choix):
    #   if isinstance(choix, list):
    #     choix = { i : choix[i] for i in range(0, len(choix) ) }
    #   if not isinstance(choix, dict):
    #     raise Exception("error: wrong ask type")
    #
    #   choix_str = msg + "\n"
    #
    #   i = 0
    #   choix_names = []
    #   for answer_name, answer in choix.items():
    #     if isinstance(answer_name, int):
    #        answer_name = answer
    #     choix_names.append(answer_name)
    #     choix_str += "[" + str(i) + "] " + answer_name + " "
    #     i += 1
    #
    #   choix_str += "\n"
    #   ret_user = input(choix_str)
    #   while ret_user not in choix_names and (int(ret_user) not in range(len(choix_names)) if RepresentsInt(ret_user) else True):
    #     error_msg = "Le message \"{}\" que vous avez rentré n'est pas pris en compte dans les réponses.\n".format(
    #       ret_user)
    #     ret_user = input(error_msg+choix_str)
    #
    #   if ret_user in choix_names:
    #     ret_user_int = choix_names.index(ret_user)
    #   else:
    #     ret_user_int = int(ret_user)
    #
    #   if get_object:
    #     choix_name = choix_names[ret_user_int]
    #     ret = [choix_name, choix[choix_name]]
    #   elif get_choice_str:
    #     ret =  choix[ret_user_int]
    #   else:
    #     ret = ret_user_int
    # else:
    #   # todo: récupération des actions dispo
    #   print("else")
    #   ret = "blabla"

    # todo : vérificaiton de sécurité du retour ?
    return

  def action(self, action_name="", others=[]):
    """
    example : personnage1.action("sortBouleDeFeu")
    Vérifie s'il a le droit de faire l'action

    :param action_name:
    :param others:
    :return:
    """

    if not action_name:
      return

    actions = self.getActions(name=action_name, with_function=True)
    action_name = list(actions)[0]
    action = actions[action_name]
    object = action[0]
    action_function = action[1]

    action_function(object, others)

  @staticmethod
  def laisser(actor, other):
    pass

  @abstractmethod
  def getActions(self, type="", name="", only_names=True, with_function=False):
    pass

  def setPosition(self, position):
    self.position = position
