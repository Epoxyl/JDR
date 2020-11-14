from Game.Classes.World.Scene import Scene
from Game.Classes.World.Actors.Meubles.Chaise import Chaise
from Game.Classes.Personnage import Personnage


class Chambre(Scene):
  hauteur = 10
  largeur = 20
  description_str = "Cellule de ???"

  def __init__(self):
    actors = []

    actors.append(Chaise([2, 2]))

    personnage = Personnage("Yohann", "Humain", "Magicien",
                            position=[4, 4])  ## todo: fonction de création de personnage

    actors.append(personnage)

    events = {
      "tour_de_garde": {
        "active": True,
        "description": "Tous les jours à 06:00, un garde passe"
      },
      "repas": {
        "active": True,
        "description": "A 12:00, un garde vous ammène à manger"
      }
    }

    super().__init__(personnage, actors, events)

  def condition_tour_de_garde(self):
    heure = "06:00"  # todo: récupération d'heure
    return heure == "06:00"

  def tour_de_garde(self):
    print("Un garde passe")
