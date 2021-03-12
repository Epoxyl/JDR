from tkinter import *
from .other_test_widget import *
import os

from .testResize import TkExample


def ppcm(*n):
  """Calcul du 'Plus Petit Commun Multiple' de n (>=2) valeurs entières (Euclide)"""

  def _pgcd(a, b):
    while b: a, b = b, a % b
    return a
  p = abs(n[0] * n[1]) // _pgcd(n[0], n[1])
  for x in n[2:]:
    p = abs(p * x) // _pgcd(p, x)
  return p

def test():
  nom = "Dragomir"
  prenom="Vlad"

  # class ExampleApp(Tk):
  #   def __init__(self):
  #     Tk.__init__(self)
  #     t = SimpleTable(self, 10, 2)
  #     t.pack(side="top", fill="x")
  #     t.replace_with_entry(1,1, Button(self, text="blabla"))
  #
  #
  # class SimpleTable(Frame):
  #   def __init__(self, parent, rows=10, columns=2):
  #     # use black background so it "peeks through" to
  #     # form grid lines
  #     Frame.__init__(self, parent, background="black")
  #     self._widgets = []
  #     for row in range(rows):
  #       current_row = []
  #       for column in range(columns):
  #         label = Label(self, text="%s/%s" % (row, column),
  #                          borderwidth=0, width=10)
  #         label.grid(row=row, column=column, sticky="nsew", padx=1, pady=1)
  #         current_row.append(label)
  #       self._widgets.append(current_row)
  #
  #     for column in range(columns):
  #       self.grid_columnconfigure(column, weight=1)
  #
  #   # def set(self, row, column, value):
  #   #   widget = self._widgets[row][column]
  #   #   widget.configure(text=value)
  #
  #   def replace_with_entry(self, row, column, widget):
  #     old_widget = self._widgets[row][column]
  #     old_widget.destroy()
  #     entry_widget = Entry(widget)
  #     print(entry_widget)
  #     entry_widget.place(x=column, y=row, anchor="nw", relwidth=1.0, relheight=1.0)
  #     entry_widget.focus_set()

  # root = Tk()
  # TkExample(root)
  # root.mainloop()

  directory = os.path.dirname(os.path.realpath(__file__)).replace('\\', '/')

  with open(directory+"/test.txt") as card:
    print(card)
    lines = card.readlines()
  print(lines)
  tab = []
  for line in lines:
    tab_split = line.split('|')
    tab.append(tab_split)
  print(tab)

  length_tab = []
  for line in tab:
    length_tab.append(len(line))
  print(length_tab)
  multiple = ppcm(*length_tab)-1
  print(multiple)

  root = Tk()  # Création de la fenêtre racine
  


  for line in range(len(tab)):
    frame = Frame(root)
    length = len(tab[line])
    prop = multiple / length
    for case in range(length):
      ## pour 8, 2 -> 1 span 4
      # 0(4) 4(4)
      # pour 8,3
      #
      col = int(case*prop)
      label = Label(root, text=str(col)+tab[line][case])
      label.grid(column=case, row=line)

  ### bordure
  # cadre = Frame(fenetre, width=768, height=576, borderwidth=1)
  # cadre.pack(fill=BOTH)
  # message = Label(cadre, text="Notre fenêtre")
  # message.pack(side="top", fill=X)

  """Premier exemple avec Tkinter.

  On crée une fenêtre simple qui souhaite la bienvenue à l'utilisateur.

  # On importe Tkinter
  from tkinter import *

  # On crée une fenêtre, racine de notre interface
  fenetre = Tk()

  # On crée un label (ligne de texte) souhaitant la bienvenue
  # Note : le premier paramètre passé au constructeur de Label est notre
  # interface racine
  champ_label = Label(fenetre, text="Salut les Zér0s !")

  # On affiche le label dans la fenêtre
  champ_label.pack()

  # On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
  fenetre.mainloop()
  
  """

  #label = Label(root, text='Personnage |')
  #label2 = Label(root, text=nom+" "+prenom)
  #label.grid(column=0, row=0)
  #label2.grid(column=1, row=0,)
  #label.grid(column=0, row=0)
  #label2.grid(column=1, row=0,)
  #label.grid(column=0, row=0)
  #label2.grid(column=1, row=0,)

  root.mainloop()  # Lancement de la boucle principale