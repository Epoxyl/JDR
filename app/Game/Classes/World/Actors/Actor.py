from abc import ABC

class Actor(ABC):
  position = []
  description = "Actor"
  actor_object = None
  actions_possibles = {}
  actions = []

  def __init__(self, position):
    """
    :param Int[] position:
    """
    self.position = position


  def description(self):
    print(self.description)

    actions_propose = self.getActions("action")


  def ask(self, msg, choix):
    """
    Affichage de question ainsi que les réponses disponibles au joueur
    :param string msg: Message/question à afficher
    :param string[] choix:
    :return:
    """

    if (choix):

      print(msg)
      choix_str = ""
      for i in range(choix):
        choix_str += "[" + i + "] " + choix[i] + " "
        #choix_str += "\n"

      ret_user = input(choix_str)
      while ret_user not in choix_str and ret_user not in range(choix_str):
        error_msg = "Le message \"{}\" que vous avez rentré n'est pas pris en compte dans les réponses.\n"
        ret_user = input(error_msg + ret_user)
    else:
      # todo: récupération des actions dispo
      print("else")

    # todo : vérificaiton de sécurité du retour ?
    return int(ret_user)