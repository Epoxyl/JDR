from functools import partial
from tkinter import *

from Game.Classes.Actors.Actor import Actor
from Game.Utils.Logs import Log
from Game.Utils.Tooltip import CreateToolTip

"""
Widget de map
"""
class MapWidget(Frame):

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
    Log.printlog(hex(id(self.active)))

    map, [max_hauteur, max_largeur] = map_infos
    scene = Frame(self, borderwidth=10, relief=RIDGE)
    width = self.winfo_width()

    width_case = int(width / max_largeur)
    # raise Exception("ici")
    champs_legend = {}
    for map_y in range(max_hauteur):
      for map_x in range(max_largeur - 1):
        case = map[map_y][map_x]
        if case == "_" or case == "|":
          case_frame = Label(scene, text=" ", bg="black", width=width_case)
        else:
          case_frame = Frame(scene, borderwidth=0.5, relief=RAISED, width=width_case)  # border
          if isinstance(case, Actor):
            case_text = case.__class__.__name__.lower()[0]
            case_label = Label(case_frame, text=case_text)
            action = partial(case.interaction, player)
            # case_label.bind("<Button>", partial(self.mapInteraction, action))
            case_label.bind("<Button>", action)
            case_label.hover = CreateToolTip(case_frame, case.short_description_str)

            champs_legend[case_text] = case.short_description_str
          else:
            case_label = Label(case_frame, text=" ")
          case_label.pack(fill=BOTH)
        case_frame.grid(row=map_y, column=map_x, sticky="nsew")

    legend = Button(scene, text="legend", command=lambda: self.legendSceneMap(champs_legend))

    legend.grid(row=max_hauteur - 1, column=max_largeur)
    scene.pack(fill=X)

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