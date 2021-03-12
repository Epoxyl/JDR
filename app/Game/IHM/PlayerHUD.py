from tkinter import *

from Game import game_directory
from Game.Utils.Logs import Log
from Game.IHM.EventWidget import EventWidget
from Game.IHM.MapWidget import MapWidget

"""
HUD du joueur
"""
class PlayerHUD:
  def __init__(self, root):
    self.fenetre = root
    self.fenetre_width = 100
    self.fenetre.geometry("800x500")
    self.top_frame = Frame(self.fenetre, borderwidth=10, relief=RIDGE)
    self.center_frame = Frame(self.fenetre, borderwidth=10, relief=RIDGE)
    self.bottom_frame = Frame(self.fenetre, borderwidth=10, relief=RIDGE)

  def loop(self):
    self.fenetre.mainloop()  # Lancement de la boucle principale

  def showHUD(self):
    # self.fenetre.geometry("600x800")
    # self.fenetre.update()
    self.top_frame.pack(fill=X)
    self.center_frame.pack(fill=BOTH, expand=YES)
    self.bottom_frame.pack(fill=X, side=BOTTOM)

  # Affichage de l'évènement
  def showEvent(self, event_name, level_name, callback):
    print(self.bottom_frame)

    self.cleanFrame(self.bottom_frame)
    EventWidget(self.bottom_frame, event_name, level_name, callback).pack()

  # Affichage du bandeau du level
  def showStartLevel(self, level, with_scene=False):
    self.cleanFrame(self.top_frame)
    description_level = level.description(self.top_frame, with_scene)
    description_level.pack()

  # affichage de la map
  def setSceneMap(self, map_infos, player):
    self.cleanFrame(self.center_frame)
    # self.center_object = MapWidget(self.center_frame, map_infos, player)
    MapWidget(self.center_frame, map_infos, player).pack(fill=BOTH, expand=YES)

  # Affichage d'une card
  def setCard(self, card_name, variable, frame):
    try:
      with open(game_directory + "/Cards/{}.txt".format(card_name)) as card_file:
        card_str = card_file.read()
      formatted_card = card_str.format(**variable)
    except FileNotFoundError as e:
      print(e)
      raise e

    self.cleanFrame(frame)
    champ_label = Label(frame, text=formatted_card, borderwidth=2)  # todo: Tableau tkinter
    champ_label.pack()

  # Clean de frame
  def cleanFrame(self, frame):
    Log.printlog("destroy")
    actual_elements = frame.winfo_children()
    for element in actual_elements:
      element.destroy()

  # Ouvre une fenêtre pour poser une question
  def getQuestion(self, personnage, msg, choix):
    question_fenetre = Tk()
    questions = Label(question_fenetre, text=msg)
    choix_frame = Frame(question_fenetre)
    for choi in list(choix.keys()):
      if isinstance(choi, int):
        choi = choix[choi]
      button = Button(choix_frame, text=choi)
      button.pack(side="left")
    questions.pack()
    choix_frame.pack()
    question_fenetre.mainloop()
