from abc import ABC, abstractmethod
import random
import json
import importlib
import Game

class Entite(ABC):
  type = ""

  vie = 0
  caracs = {}

  nom = ""
  race = None
  sexe = ""
  force = 0
  dexterite = 0
  consistance = 0
  intelligence = 0
  sagesse = 0
  charisme = 0
  initiative = 0
  defaultAttack = None
  equipements = {
    "TETE": None, "MAIN1": None, "MAIN2": None, "CORPS": None, "JAMBES": None
  }
  inventaire = {}

  def __init__(self, nom, race="Humain", sexe="homme", type="Jouables"):  ##constructeur
    self.nom = nom
    module = importlib.import_module("Game.Classes.Races." + type + "." + race)
    module_class = getattr(module, race)
    self.race = module_class()
    self.setDefaultAttack()
    self.sexe = sexe
    self.type = type
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

    # Ajout des modificateurs de races, présents dans races_Jouables.json
    with open(directory + "/Classes/Races/races_"+self.type+".json") as races_modifieurs:
      modifieurs_races = json.load(races_modifieurs)
    modifieurs_race = modifieurs_races[race]

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

  def takeDamage(self, damage):
      self.vie -= damage

  def testAction(self, type, difficulte, modifieurs=0):
    jet_de = random.randint(1, 20)
    result = jet_de + self.caracs[type] + modifieurs
    if jet_de == 20:
      # Reussite critique
      return 2
    elif result >= difficulte:
      # Reussite Classique
      return 1
    elif result == 1:
      # Echec Critique
      return -1
    else:
      # Echec Classique
      return 0

  def testType(self, type, modifieurs=0):
    jet_de = random.randint(1, 20)
    return jet_de + self.caracs[type] + modifieurs

  @staticmethod
  def calculateStat(modifieur):
      rand = random.randint(0,1)
      return(10 + modifieur*2+rand)

  def tourCombat(self, combat, joueur_informations):
    """
    Action d'un tour de combat avec le personnage
    :param combat: instance de Combat
    :param joueur_informations:
    :return:
    """
    action_combat = "Attaquer"
    if action_combat == "Attaquer":
      ennemis = combat.getEnnemies(joueur_informations)
      #### ICI POUR CHOISIR L'ennemi
      ennemy_chosen = ennemis[0]
      ##### ICI POUR CHOISIR l'action
      attaque = self.defaultAttack
      attaque(self, ennemy_chosen)
