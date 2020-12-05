from functools import partial
from tkinter import Frame, Label, Button, BOTH

from Game import game_directory
from Game.Utils.Logs import Log

"""
Widget d'évènement
"""
class EventWidget(Frame):
  current_page = 0
  pages = []

  def __init__(self, parent, event_name, level_name, callback):
    """
    Widget d'évènement
    :param parent: Parent du widget
    :param event_name: Nom de l'évènement
    :param level_name: Nom du niveau
    :param callback: callback à lancer à la fin de l'évènement
    """
    Frame.__init__(self, parent)
    self.callback = callback

    with open(game_directory + "/Levels/{}/Events/{}.txt".format(level_name, event_name)) as event_file:
      for page in event_file.read().split("[...]"):
        self.pages.append(page)
    self.showPage(0)


  def showPage(self, page_number):
    """
    Affiche la page de description de l'evenement, et le bouton "next"
    :param page_number: numéro de la page
    :return:
    """
    for widget in self.winfo_children():
      widget.destroy()

    content = Label(self, text=self.pages[page_number])
    content.pack()

    if page_number >= len(self.pages)-2:

      on_click = self.callback
    else:
      on_click = partial(self.showPage, page_number+1)
    next_Button = Button(self, text="NEXT", command= on_click)
    next_Button.pack(fill=BOTH)
