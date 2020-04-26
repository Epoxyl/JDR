from abc import ABC, abstractmethod
from Game.Classes.Jobs.Magicien import Magicien
from Game.Classes.Entite import Entite
import Game
import importlib
import random
import json
import os

class Personnage(Entite):
    """Classe de base pour les personnages"""


    def action(self, action_name, parameters={}):
        """
        example : personnage1.action("sortBouleDeFeu")

        :param action_name:
        :param parameters:
        :return:
        """

        module = importlib.import_module("Game.Classes.Jobs."+self.job)
        module_class = getattr(module, self.job)
        module_function = getattr(module_class, action_name)
        if module_function:
            return module_function(self, **parameters)

        module = importlib.import_module("Game.Classes.Personnage")
        module_class = getattr(module, "Personnage")
        module_function = getattr(module_class, action_name)
        if module_function:
            return module_function(self, **parameters)

    def takeDamage(self, damage):
        self.vie -= damage

    def getModifieur(self, name_val):
        return self.caracs[name_val]

    @staticmethod
    def calculateStat(modifieur):
        rand = random.randint(0,1)
        return(10 + modifieur*2+rand)

    def __str__(self):
        msg = ""
        msg += "nom : "+str(self.nom)+"\n"
        msg += "race : "+str(self.race)+"\n"
        msg += "job : "+str(self.job)+"\n"
        msg += "sexe : "+str(self.sexe)+"\n"
        msg += "force : "+str(self.force)+"\n"
        msg += "dexterite : "+str(self.dexterite)+"\n"
        msg += "consistance : "+str(self.consistance)+"\n"
        msg += "intelligence : "+str(self.intelligence)+"\n"
        msg += "sagesse : "+str(self.sagesse)+"\n"
        msg += "charisme : "+str(self.charisme)

        return msg