from Game.Classes.Actors.Actor import Actor

class Chaise(Actor):
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