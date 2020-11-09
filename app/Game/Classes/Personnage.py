from abc import ABC, abstractmethod
from Classes.Entite import Entite
import Game
import importlib
import random
import json
import os

class Personnage(Entite):
  """Classe de base pour les personnages"""

  job = None

  def __init__(self, name="", race="Humain", job="Guerrier", sexe="Homme", age="25"):
    module = importlib.import_module("Classes.Jobs." + job)
    module_class = getattr(module, job)
    self.job = module_class()
    self.age = age
    self.vie = self.job.getVie()
    super().__init__(name, race, sexe, type="Jouables")

  def setDefaultAttack(self, defaultAttack=""):
    if not defaultAttack:
      functions = self.job.getFunctions()                                ####### L'ENIGME DU COMMIT
      print(functions)
      defaultAttack_string = functions[0][1]
      self.defaultAttack = getattr(self.job, defaultAttack_string)
    else:
      defaultAttack = getattr(self.job, defaultAttack)
      self.defaultAttack = defaultAttack
      ### Faire le cas où l'action est dans les equipements/races

  def action(self, action_name, parameters={}):
    """
    example : personnage1.action("sortBouleDeFeu")

    :param action_name:
    :param parameters:
    :return:
    """

    functions = self.job.getFunctions()
    print(functions)
    #module_class = getattr(module, self.job)
    #action_function = getattr(module_class, action_name)
    #if not action_function:
    #  module = importlib.import_module("Classes.Personnage")
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
