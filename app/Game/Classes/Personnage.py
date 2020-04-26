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

        module = importlib.import_module("Game.Classes.Jobs."+self.job)
        module_class = getattr(module, self.job)
        action_function = getattr(module_class, action_name)
        if not action_function:
            module = importlib.import_module("Game.Classes.Personnage")
            module_class = getattr(module, "Personnage")
            action_function = getattr(module_class, action_name)

        if action_function:
            infos_action = getattr(module_class, "infos_"+action_name)
            difficulte = 0
            if "target" in parameters.keys():
                target = parameters["target"]
                if type(target).__name__ == "Entite":
                    difficulte = target.defense
            if not difficulte:
                difficulte = infos_action["difficulte"]

            result = self.testAction(infos_action["type"], difficulte)  # modifieurs testAction ?
            action_function(self, **parameters)

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