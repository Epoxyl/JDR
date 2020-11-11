from abc import ABC, abstractmethod
import random
import json
import importlib
from Game import game_directory
from Game.Classes.World.Actors.Actor import Actor

class Entite(Actor):
  type = ""

  vie = 100
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

  def __init__(self, nom, race="Humain", sexe="homme", type="Jouables", position=[0,0]):  ##constructeur
    """
    :param str nom:
    :param str race:
    :param str sexe:
    :param str type:
    """

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

    # Ajout des modificateurs de races, présents dans races_Jouables.json
    with open(game_directory + "/Classes/Races/races_"+self.type+".json") as races_modifieurs:
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
    #print(caracs)

    super().__init__(position)

  def takeDamage(self, damage):
      self.vie -= damage

  def getActions(self, type="", name="", only_names=False, with_function = False):
    """
    Récupère les actions possibles suivant le type et le nom
    :param string type: Type d'utilisation
    :param string name: Nom de l'action
    :param bool only_names: retourne uniquement les noms des actions (pour l'affichage)
    :return actions:
    """
    actions_race = self.race.getActions(type, name, only_names, with_function)

    #todo : actions_equipements

    return actions_race

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

  @abstractmethod
  def setDefaultAttack(self):
    pass
