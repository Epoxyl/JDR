from abc import ABC, abstractmethod
from Game.Classes.Entite import Entite
import Game
import importlib
import random
import json
import os

class Personnage(Entite):
  """Classe de base pour les personnages"""
  job = ""

  def __init__(self, name="", race="Humain", job="Guerrier", sexe="Homme", age="25"):
    self.job = job
    self.age = age
    super().__init__(name, race, sexe, "Jouables")

  def action(self, action_name, parameters={}):
    """
    example : personnage1.action("sortBouleDeFeu")

    :param action_name:
    :param parameters:
    :return:
    """

    module = importlib.import_module("Game.Classes.Jobs." + self.job)
    module_class = getattr(module, self.job)
    action_function = getattr(module_class, action_name)
    if not action_function:
      module = importlib.import_module("Game.Classes.Personnage")
      module_class = getattr(module, "Personnage")
      action_function = getattr(module_class, action_name)

    # for equipement in self.equipements:
    #   module_class = type(equipement)
    #    action_function = getattr(module_class, action_name)
    #    if action_function:
    #      pass
    #
    if action_function:
      infos_action = getattr(module_class, "infos_" + action_name)
      difficulte = 0
      if "target" in parameters.keys():
        target = parameters["target"]
        if type(target).__name__ == "Entite":
          difficulte = target.defense
      if not difficulte and "difficulte" in infos_action.keys():
        difficulte = infos_action["difficulte"]

      result = self.testAction(infos_action["type"], difficulte)  # modifieurs testAction ?
      action_function(self, **parameters)

  def setEquipement(self, equipement, emplacement_voulu = "", deux_mains=False):
    print("set equip")
    if not emplacement_voulu:
      emplacement_voulu = equipement.emplacement

    if emplacement_voulu == "MAIN":
      if not self.equipements["MAIN1"]:
        self.equipements["MAIN1"] = equipement
      ## Double main et remplacement d'arme à gérer

    if emplacement_voulu in self.equipements.keys():
      return self.replaceEquipement(equipement)

    if emplacement_voulu not in self.equipements.keys():
      # Emplacement erroné
      return False




  def replaceEquipement(self, equipement, emplacement=""):
    print("replace"+equipement)
    if not emplacement:
      emplacement = equipement.emplacement

    if emplacement in self.equipements.keys():
      old_equipement = self.equipements[emplacement]
    else:
      # emplecement erroné !
      return False
    self.equipements[emplacement] = equipement
    if old_equipement:
      return self.storeObject(old_equipement, 1)
    return True

  def storeObject(self, objet, nombre):
    print("Ajoute "+objet)
    return True

  def getModifieur(self, name_val):
    return self.caracs[name_val]

  @staticmethod
  def calculateStat(modifieur):
    rand = random.randint(0, 1)
    return (10 + modifieur * 2 + rand)

  def __str__(self):
    msg = self.nom + "({})".format(self.job)

    return msg

  def toString(self):
    msg = ""
    msg += "nom : " + str(self.nom) + "\n"
    msg += "race : " + str(self.race) + "\n"
    msg += "job : " + str(self.job) + "\n"
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

    msg += "force : " + str(self.force) + "\n"
    msg += "dexterite : " + str(self.dexterite) + "\n"
    msg += "consistance : " + str(self.consistance) + "\n"
    msg += "intelligence : " + str(self.intelligence) + "\n"
    msg += "sagesse : " + str(self.sagesse) + "\n"
    msg += "charisme : " + str(self.charisme)

    return msg
