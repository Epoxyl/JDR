from abc import ABC, abstractmethod
from Game.Classes.Entite import Entite
import Game
import importlib
import random
import json
import os

class Personnage(Entite):
  """Classe de base pour les personnages"""

  job = None

  def __init__(self, name="", race="Humain", job="Guerrier", sexe="Homme", age=25, position=[0,0]):
    """

    :param str name:
    :param str race:
    :param str job:
    :param str sexe:
    :param int age:
    :param position:
    """
    module = importlib.import_module("Game.Classes.Jobs." + job)
    module_class = getattr(module, job)
    self.job = module_class()
    self.age = age
    self.vie = self.job.getVie()
    super().__init__(name, race, sexe, "Jouables", position)

  def setDefaultAttack(self, defaultAttack=""):
    if not defaultAttack:
      actions = self.getActions(only_names=True, type="combat")                                ####### L'ENIGME DU COMMIT
      print(actions)
      defaultAttack_string = actions[0]
      self.defaultAttack = getattr(self.job, defaultAttack_string)
    else:

      defaultAttack = getattr(self.job, defaultAttack)
      self.defaultAttack = defaultAttack
      ### Faire le cas où l'action est dans les equipements/races
      print(self.defaultAttack)

  def action(self, action_name, parameters={}):
    """
    example : personnage1.action("sortBouleDeFeu")
    Vérifie s'il a le droit de faire l'action

    :param action_name:
    :param parameters:
    :return:
    """

    if not action_name:
      return

    if not isinstance(parameters, list):
      print("here")
      parameters = {parameters}
    print(parameters)
    print(type(self))
    actions = self.getActions(name=action_name, only_names=True, with_function=True)
    action = actions[0]
    print(action)
    action_function = action[2]
    object = action[1]
    action_function(object, *parameters)
    #if not action_function:
    #  module = importlib.import_module("Game.Classes.Personnage")
    #  module_class = getattr(module, "Personnage")
    #  action_function = getattr(module_class, action_name)

    # for equipement in self.equipements:
    #   module_class = type(equipement)
    #    action_function = getattr(module_class, action_name)
    #    if action_function:
    #      pass
    #
   #if action_function:
   #  infos_action = getattr(module_class, "infos_" + action_name)
   #  difficulte = 0
   #  if "target" in parameters.keys():
   #    target = parameters["target"]
   #    if type(target).__name__ == "Entite":
   #      difficulte = target.defense
   #  if not difficulte and "difficulte" in infos_action.keys():
   #    difficulte = infos_action["difficulte"]

   #  result = self.testAction(infos_action["type"], difficulte)  # modifieurs testAction ?
   #  action_function(self, **parameters)

  def getActions(self, type="", name="", only_names=False, with_function = False):
    """
    Récupère les actions possibles suivant le type et le nom
    :param string type: Type d'utilisation
    :param string name: Nom de l'action
    :param bool only_names: retourne uniquement les noms des actions (pour l'affichage)
    :return actions:
    """
    actions_job = self.job.getActions(type, name, only_names, with_function)

    return actions_job + super().getActions(type, name, only_names, with_function)

  def setEquipement(self, equipement, emplacement_voulu="", deux_mains=False):
    """
    Ajoute un equipement
    :param equipement:
    :param emplacement_voulu: clef du tableau Entite.equipements
    :param deux_mains: Permet de s'équiper de l'arme à deux mains
    :return:
    """
    if not emplacement_voulu:
      emplacement_voulu = equipement.emplacement

    if "MAIN" in emplacement_voulu:
      if self.equipements["MAIN1"] and deux_mains:
        return self.replaceEquipement(equipement, "MAIN2")

      if emplacement_voulu == "MAIN":
        emplacement_voulu+="1"
      return self.replaceEquipement(equipement, emplacement_voulu)
      ## Double main et remplacement d'arme à gérer

    if emplacement_voulu in self.equipements.keys():
      return self.replaceEquipement(equipement, emplacement_voulu)

    if emplacement_voulu not in self.equipements.keys():
      # Emplacement erroné
      return False

  def replaceEquipement(self, equipement, emplacement=""):
    """
    Remplace un équipement et place le précédent equipement dans l'inventaire
    :param equipement:
    :param emplacement:
    :return:
    """
    print("place/replace "+equipement.__str__())
    if not emplacement:
      emplacement = equipement.emplacement
    if emplacement in self.equipements.keys():
      old_equipement = self.equipements[emplacement]
    else:
      print("emplecement erroné !")
      return False

    self.equipements[emplacement] = equipement
    if old_equipement:
      return self.storeObject(old_equipement)
    return True

  def storeObject(self, objet):
    """
    Place un objet dans l'inventaire
    :param objet:
    :return:
    """
    print("Ajoute "+objet.__str__())
    self.inventaire[objet.nom] = objet
    return True

  def getModifieur(self, type):
    """
    Récupère le modifieur d'un type
    :param type: type du modifieur (exemple FOR)
    :return:
    """
    return self.caracs[type]

  @staticmethod
  def calculateStat(modifieur):
    rand = random.randint(0, 1)
    return (10 + modifieur * 2 + rand)

  def __str__(self):
    msg = self.nom + "({})".format(self.job)+"\n"
    msg += str(self.vie) + "PV"
    return msg

  def toString(self):
    msg = ""
    msg += "nom : " + str(self.nom) + "\n"
    msg += "race : " + str(self.race) + "\n"
    msg += "job : " + self.job + "\n"
    msg += "sexe : " + str(self.sexe) + "\n"
    msg += "\n"
    for partie in self.equipements.keys():
      if self.equipements[partie]:
        msg += partie+": "+self.equipements[partie].__str__()
        if partie == "MAIN1":
          msg += "(D)"
        elif partie == "MAIN2":
          msg += "(G)"
        msg += "\n"
    msg += "\n"
    msg += "Inventaire : \n"
    for objet in self.inventaire.keys():
      msg += self.inventaire[objet].__str__()
    msg += "\n"
    msg += "force : " + str(self.force) + "\n"
    msg += "dexterite : " + str(self.dexterite) + "\n"
    msg += "consistance : " + str(self.consistance) + "\n"
    msg += "intelligence : " + str(self.intelligence) + "\n"
    msg += "sagesse : " + str(self.sagesse) + "\n"
    msg += "charisme : " + str(self.charisme)

    return msg
