from tkinter import Tk, Label

from Game import game_directory

fenetre = Tk()

def showHUD(main_frame=None, left_frame=None, right_frame=None, bottom_frame=None):

  fenetre.mainloop()  # Lancement de la boucle principale


def getCard(card_name, variable):
  try :
    with open(game_directory + "/Cards/{}.txt".format(card_name)) as card_file:
      card_str = card_file.read()
    formatted_card = card_str.format(**variable)
  except FileNotFoundError as e:
    print(e)
    raise e
  champ_label = Label(fenetre, text=formatted_card, borderwidth=2) #todo: Tableau tkinter
  return champ_label

def getSceneMap(map_str):
  map_label = Label(fenetre, text=map_str, borderwidth=2) #todo: Tableau tkinter
  return map_label