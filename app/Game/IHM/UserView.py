from tkinter import Tk, Label, Frame, BOTH, Button
from functools import partial
from Game import game_directory
from Game.Classes.Actors.Actor import Actor
from Game.Utils.Tooltip import CreateToolTip

class UserView():
  fenetre = Tk()

  def __init__(self):
    # self.fenetre.geometry("600x600")
    pass

  def loop(self):
    self.fenetre.mainloop()  # Lancement de la boucle principale

  def cleanFenetre(self):
    actual_elements = self.fenetre.winfo_children()
    for element in actual_elements:
      element.destroy()

  def showHUD(self, main_frame=None, left_frame=None, right_frame=None, bottom_frame=None):
    if left_frame:
      left_frame.pack()
    if main_frame:
      main_frame.pack()
    if right_frame:
      right_frame.pack()

  def showEvent(self, event_name, level_name):
    with open(game_directory+"/Levels/{}/Events/{}.txt".format(level_name, event_name)) as event_file:
      for line in event_file.read().split("[...]"):
        self.cleanFenetre()

        # self.cleanFenetre()
        # line_frame = Label(self.fenetre, line)
        # line_frame.bind("<Button>", )


  def showStartLevel(self, level, frame=None):
    if not frame:
      frame = self.fenetre
    level_frame = Frame(frame)
    description_level = level.description(level_frame)
    description_level.pack()

    return frame

  def getCard(self, card_name, variable):
    try:
      with open(game_directory + "/Cards/{}.txt".format(card_name)) as card_file:
        card_str = card_file.read()
      formatted_card = card_str.format(**variable)
    except FileNotFoundError as e:
      print(e)
      raise e
    champ_label = Label(self.fenetre, text=formatted_card, borderwidth=2)  # todo: Tableau tkinter
    return champ_label

  def getSceneMap(self, map, player):
    cadre = Frame(self.fenetre, width=768, height=576, borderwidth=1)
    cadre.pack(fill=BOTH)

    scene = Frame(cadre)
    for line_map in map:
      line_frame = Frame(scene)
      for case in line_map:
        if isinstance(case, Actor):
          case_frame = Label(line_frame, text=case.__class__.__name__.lower()[0])
          case_frame.bind("<Button>", partial(case.interaction, player))

          case_frame.hover = CreateToolTip(case_frame, case.short_description_str)
        else:
          case_frame = Label(line_frame, text="")
        case_frame.pack(side="left")

      line_frame.pack()

    return scene

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
