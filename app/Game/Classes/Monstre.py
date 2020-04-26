from Game.Classes.Entite import Entite
from abc import ABC, abstractmethod
import importlib
class Monstre(Entite):
  equipement = {
  }

  def __init__(self, name="", race="Humain", sexe="Homme"):
    print("I am born !")
    super().__init__(name, race, sexe, "Mobs")

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