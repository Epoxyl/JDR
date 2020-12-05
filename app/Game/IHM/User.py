from functools import partial
from tkinter import Tk, Frame

from Game.IHM.PlayerHUD import PlayerHUD, RAISED


class User():
  def __init__(self, level):
    self.player_hud = PlayerHUD(Tk())
    self.current_level = level

  # Lancement du niveau courant
  def launchLevel(self):
    self.player_hud.showStartLevel(self.current_level)
    self.current_level.launch(player_hud=self.player_hud)

  # Affichage du characterHUD classique
  def setCharacterHUD(self, personnage, scene):
    self.player_hud.showStartLevel(self.current_level, with_scene=True)
    self.player_hud.setSceneMap(scene.getMap(), personnage)
    self.setCharacterInfos(personnage)

    self.player_hud.showHUD()

  #todo : Autres fonctions de PlayerHUD (Controller) ?

  # Affichage des informations de l'utilisateur
  def setCharacterInfos(self, personnage):
    self.player_hud.setCard("personnage", variable={"nom":personnage.nom, "age": personnage.age, "job": personnage.job, "level": 103}, frame=self.player_hud.bottom_frame)

  # Ouvre une fenêtre pour poser une question
  def askQuestion(self, personnage, msg, choix=None, get_choice_str=False, get_object=False):
    if (choix):
      if isinstance(choix, list):
        choix = {i: choix[i] for i in range(0, len(choix))}
      if not isinstance(choix, dict):
        raise Exception("error: wrong ask type")

      choix_str = msg + "\n"

      choix_names = []
      for answer_name, answer in choix.items():
        if isinstance(answer_name, int):
          answer_name = answer
        choix_names.append(answer_name)

      frame_questions = self.player_hud.getQuestion(personnage, msg, choix)
