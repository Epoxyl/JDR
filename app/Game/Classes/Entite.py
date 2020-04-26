from abc import ABC, abstractmethod
import json
import Game

class Entite(ABC):
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
    with open(directory + "/Classes/races.json") as races_modifieurs:
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