from tkinter import *
import os


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


  #label = Label(root, text='Personnage |')
  #label2 = Label(root, text=nom+" "+prenom)
  #label.grid(column=0, row=0)
  #label2.grid(column=1, row=0,)
  #label.grid(column=0, row=0)
  #label2.grid(column=1, row=0,)
  #label.grid(column=0, row=0)
  #label2.grid(column=1, row=0,)

  root.mainloop()  # Lancement de la boucle principale