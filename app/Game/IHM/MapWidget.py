from functools import partial
from tkinter import *

from Game.Classes.Actors.Actor import Actor
from Game.Utils.Logs import Log
from Game.Utils.Tooltip import CreateToolTip

"""
Widget de map
"""
class MapWidget(Frame):
  height = 20
  width = 80

  def __init__(self, root, map_infos, player, active=True):
    """
    Widget de map
    :param root: Parent de la map
    :param map_infos:
    :param player:
    :param active: Possibilité de faire des actions ou non
    """
    Frame.__init__(self, root)
    self.active = active

    map, [max_hauteur, max_largeur] = map_infos

    scene = Frame(self)
    champs_legend = {}
    for map_y in range(max_hauteur):
      for map_x in range(max_largeur - 1):
        case = map[map_y][map_x]
        case_frame = Frame(scene, borderwidth=0.5, relief=RAISED)
        if case == "_" or case == "|":
          case_widget = Label(case_frame, text=" ", bg="black")
        else:
          case_widget = Frame(case_frame)  # border
          if isinstance(case, Actor):
            case_text = case.__class__.__name__.lower()[0]
            case_label = Label(case_widget, text=case_text)
            action = partial(case.interaction, player)
            # case_label.bind("<Button>", partial(self.mapInteraction, action))
            case_label.bind("<Button>", action)
            case_label.hover = CreateToolTip(case_widget, case.short_description_str)
            case_label.pack(fill=BOTH, expand=YES)
            champs_legend[case_text] = case.short_description_str
          else:
            case_widget = Label(case_frame, text=" ")
        case_widget.pack(fill=BOTH, expand=YES)
        case_frame.grid(row=map_y, column=map_x, sticky="nsew")

    legend = Button(scene, text="legend", command=lambda: self.legendSceneMap(champs_legend))

    for i in range(max_hauteur):
      scene.grid_rowconfigure(i, weight=1)
    for i in range(max_largeur-1):
      scene.grid_columnconfigure(i, weight=1)

    legend.grid(row=0, column=max_largeur - 2, sticky="nsew")
    scene.pack(fill=BOTH, expand=YES)

  # def mapInteraction(self, function):
  #   if not self.active:
  #     return False
  #
  #   function()

  def legendSceneMap(self, champs=None):

    legend_fenetre = Tk()
    for champ_key, champ in champs.items():
      text = f"{champ_key} : {champ}"
      label = Label(legend_fenetre, text=text)
      label.pack()

    legend_fenetre.mainloop()