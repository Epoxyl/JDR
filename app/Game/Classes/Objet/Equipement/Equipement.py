from abc import ABC, abstractmethod
import json
import Game


class Equipement(ABC):

  durabilite=0
  poids=0
  nom=""
  prix=0
  description=""

  def __init__(self,nom,prix,description,durabilite,poids):
    self.nom = nom
    self.prix = prix
    self.descritpion = description
    self.durabilite=durabilite
    self.poids=poids

