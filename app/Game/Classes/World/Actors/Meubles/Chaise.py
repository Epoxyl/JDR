from Game.Classes.World.Actors.Actor import Actor

class Chaise(Actor):
  position = [0, 0]
  actions_meuble = {
    "s_assoir": {
      "active": True
    }
  }

  def s_assoir(self, Actor):
    """
    :param joueur: Actor de l'action
    :return:
    """

    reponse = Actor.ask("Voulez-vous vous assoir ?", ["Oui", "Non"])
    if (reponse == 0):
      # joueur.setPosition(self.position) todo: fonction setPosition sur Actor (et hériter ?)
      print("Vous avez plus important à faire que vous assoir !")
