from Game.Classes.World.Actors.Actor import Actor
from Game.Classes.World.Actors.Meubles.Meuble import Meuble


class Chaise(Meuble):
  description_str = "Une chaise en bon état, elle donne envie de s'assoir dessus"
  interactions_meuble = {
    "s_assoir": {
      "active": True
    }
  }

  @staticmethod
  def s_assoir(object, actor):
    """
    :param Actor actor: Actor de l'action
    :return:
    """

    # actor.setPosition(object.position)
    print("Vous avez plus important à faire que vous assoir !")
