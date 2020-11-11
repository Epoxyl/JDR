from Game.Classes.World.Scene import Scene
from Game.Classes.World.Actors.Meubles.Chaise import Chaise
from Game.Classes.Personnage import Personnage

class Prison(Scene):


  def __init__(self, hauteur=0, largeur=0,):
    actors = []

    actors.append(Chaise([2,2]))

    personnage = Personnage("Yohann", "Humain", "Magicien", position=[1,2])  ## todo: fonction de création de personnage

    actors.append(personnage)

    super().__init__(hauteur, largeur, actors)