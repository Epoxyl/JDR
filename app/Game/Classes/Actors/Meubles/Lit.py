from Game.Classes.Actors.Actor import Actor
from Game.Classes.Actors.Meubles.Meuble import Meuble


class Lit(Meuble):
  short_description_str = "Lit"
  description_str = "Un lit en bon état, il donne envie de piquer un somme"
  interactions_meuble = {
    "s_assoir": {
      "active": True
    },
    "dormir": {
      "active": True
    }
  }

  @staticmethod
  def s_assoir(object, Actor):
    """
    :param Actor Actor: Actor de l'action
    :return:
    """

    # joueur.setPosition(self.position) todo: fonction setPosition sur Actor (et hériter ?)
    print("Vous avez plus important à faire que vous assoir !")

  @staticmethod
  def dormir(object, Actor):
    """
    :param Actor Actor:
    :return:
    """

    reponse = Actor.ask("Voulez-vous dormir ?", ["Oui", "Non"])
    if (reponse == 0):
      # joueur.setPosition(self.position) todo: fonction setPosition sur Actor (et hériter ?)
      print("Vous avez plus important à faire que de dormir !")