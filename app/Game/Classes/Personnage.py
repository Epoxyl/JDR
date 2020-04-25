from abc import ABC, abstractmethod


class Personnage(ABC):
    """Classe de base pour les personnages"""
    force = 0
    vie = 0
    race = "humain"


    def __init__(self, nom, race, job, sexe):  ##constructeur
        self.nom = nom
        self.race = race
        self.job = job
        self.sexe = sexe

    def ajustAttributes(self):
        self.force = 12