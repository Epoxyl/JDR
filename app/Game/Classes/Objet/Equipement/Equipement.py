from abc import ABC, abstractmethod
import json
import Game


class Equipement(ABC):
  durabilite=0
  poids=0
  nom=""
  prix=0
  description=""
  emplacement = ""
  double_mains = False

  def __init__(self, nom, prix, description, durabilite, poids, emplacement):
    self.nom = nom
    self.prix = prix
    self.descritpion = description
    self.durabilite=durabilite
    self.poids=poids
    self.emplacement = emplacement

  def __str__(self):
    msg = self.nom
    return msg

  def defaultAttack(self, Character, target):
    print("defaultAttack")
    degats = 4
    target.takeDamage(degats)