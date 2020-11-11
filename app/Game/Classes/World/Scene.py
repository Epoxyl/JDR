class Scene():
  """

  """
  hauteur = 1
  largeur = 1

  events = {}  # Liste d'évènements par nom d'objet (example: "coffre": "ouvrir", "porter", "détruire")
  actors = []

  # biome = "cave"

  def __init__(self, hauteur=1, largeur=1, actors=[], events={}):
    self.hauteur = hauteur
    self.largeur = largeur
    self.actors = actors
    self.events = events

    # todo: générateur à hauteur/largeur (par la superficie) et ennemies

  def displayScnene(self):

    # todo: displaySceneForFights
    actors_by_position = self.getActors(with_position=True)

    msg = " " + "_" * self.largeur + "\n"
    line = ""
    for y in range(self.hauteur):
      line = "|"
      for x in range(self.largeur):
        if [x, y] in actors_by_position[0]:
          line += "o"
        else:
          line += " "
      line += "|\n"
      msg += line
    msg += " " + "_" * self.largeur + "\n"
    print(msg)

  def getActors(self, with_position=False, only_position=False):
    if only_position:
      return [actor.position for actor in self.actors]
    elif with_position:
      return [[actor.position, actor] for actor in self.actors]

    return self.actors
