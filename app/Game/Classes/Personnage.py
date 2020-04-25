from abc import ABC, abstractmethod


class Personnage(ABC):
    """Classe de base pour les personnages"""

    def __init__(self, nom, race, sexe):  ##constructeur
        self.nom = nom
        self.race = race
        self.sexe = sexe
