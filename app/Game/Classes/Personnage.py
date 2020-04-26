from abc import ABC, abstractmethod
from Game.Classes.Jobs.Magicien import Magicien
import Game
import importlib
import random
import json
import os

class Personnage(ABC):
    """Classe de base pour les personnages"""
    vie = 0
    caracs = {}

    nom = ""
    race = ""
    job = ""
    sexe = ""
    force = 0
    dexterite = 0
    consistance = 0
    intelligence = 0
    sagesse = 0
    charisme = 0

    def __init__(self, nom, race="Humain", job="Magicien", sexe="homme"):  ##constructeur
        self.nom = nom
        self.race = race
        self.job = job
        self.sexe = sexe
        ## CES VALEURS A DETERMINER DE MANIERE ALEATOIRE
        caracs = {
            "FOR": 1,
            "DEX": 1,
            "CON": 2,
            "INT": -1,
            "SAG": 1,
            "CHA": 2
        }

        directory = Game.directory

        # Ajout des modificateurs de races, présents dans races.json
        with open(directory+"/Classes/races.json") as races_modifieurs:
          modifieurs_races = json.load(races_modifieurs)
        modifieurs_race = modifieurs_races[self.race]

        for name_cara in ["FOR", "DEX", "CON", "INT", "SAG", "CHA"]:
            if name_cara in modifieurs_race:
                caracs[name_cara] += modifieurs_race[name_cara]

        self.force = self.calculateStat(caracs["FOR"])
        self.dexterite = self.calculateStat(caracs["DEX"])
        self.consistance = self.calculateStat(caracs["CON"])
        self.intelligence = self.calculateStat(caracs["INT"])
        self.sagesse = self.calculateStat(caracs["SAG"])
        self.charisme = self.calculateStat(caracs["CHA"])

        self.caracs = caracs
        print(caracs)


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
            module_function(self, **parameters)
        else:
            print("Le personnage ne connait pas l'attaque")

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