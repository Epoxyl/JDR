from Game.Classes.Entite import Entite
from abc import ABC, abstractmethod
import importlib
class Monstre(Entite):
  initiative = 0
  equipement = {
  }

  def __init__(self, nom="", race="Humain", sexe="Homme"):
    print("I am born !")
    super().__init__(nom=nom, race=race, sexe=sexe, type="Mobs")

  def setDefaultAttack(self, defaultAttack=""):
    if not defaultAttack:
      functions = self.race.getFunctions()
      print(functions)
      defaultAttack_string = functions[0][1]
      self.defaultAttack = getattr(self.race, defaultAttack_string)
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

      module = importlib.import_module("Game.Classes.Races.Mobs."+self.race)
      module_class = getattr(module, self.job)
      module_function = getattr(module_class, action_name)
      if module_function:
          return module_function(self, **parameters)

      module_function = getattr(self.__class__, action_name)
      if module_function:
          return module_function(self, **parameters)

  def __str__(self):
    msg = self.nom+"({})".format(str(self.race))
    return msg