from Game import game_directory, session
from Game.Utils.Session import Session


class Scene():
  """

  """
  max_hauteur = 1
  max_largeur = 1
  starting_event = ""
  description_str = ""
  player = None
  name = ""

  events = {}  # Liste d'évènements par nom d'objet (example: "coffre": "ouvrir", "porter", "détruire")
  actors = []

  # biome = "cave"

  def __init__(self, player=None, actors=[], events={}):
    self.actors = actors
    self.events = events
    self.player = player
    self.name = self.__class__.__name__

    self.loadEmptyMap()

    # todo: générateur à hauteur/largeur (par la superficie) et ennemies

  def listActors(self, with_objects=False):
    """
    Liste les actors de la scène
    :param bool with_objects: Avec les actors
    :return:
    """

    return {actor.__class__.__name__: actor if with_objects else actor.__class__.__name__ for actor in self.actors}

  def chooseActor(self, asking_actor):
    """

    :param Actor asking_actor: Player effectuant l'action
    :return Actor:
    """
    actors = self.listActors(True)
    del actors[asking_actor.__class__.__name__]
    return asking_actor.ask(self.description_str + "\nAvec quoi voulez-vous interagir ?", actors, get_object=True)

  def description(self, asking_actor=None):
    """
    Affiche la description et retourne l'Actor choisi par l'utilisateur
    :param Actor asking_actor: Player effectuant l'action
    :return Actor:
    """
    if not asking_actor:
      asking_actor = self.player
    Session.get("User").setCharacterHUD(self.player, self)
    if self.starting_event:
      server = Session.get("Server")
      server.event(self.starting_event, self.player)
    return

  def loadEmptyMap(self):
    """
    Load the empty map as list
    :return list:
    """
    map_file = open(game_directory+"/Levels/Prison/Scenes/{}_map.txt".format(self.name.lower()))
    lines = map_file.readlines()
    self.max_largeur = max([len(line) for line in lines])
    self.max_hauteur = len(lines)
    return [list(line) for line in lines]

  def getMap(self):
    map = self.loadEmptyMap()
    for actor in self.actors:
      map[actor.position[0]][actor.position[1]] = actor
    return(map, [self.max_hauteur, self.max_largeur])

  def displayScene(self):
    """
    display the scene with actors for User View
    :return:
    """

    # todo: displaySceneForFights
    actors = self.listActors(with_objects=True)
    actors_by_position = {str(actor.position): actor for actor in actors.values()}

    msg = " " + "_" * self.max_largeur + "\n"
    line = ""
    for y in range(self.hauteur):
      line = "|"
      for x in range(self.max_largeur):
        if "[{}, {}]".format(x,y) in actors_by_position.keys():
          actor = actors_by_position["[{}, {}]".format(x,y)]
          actor_name = actor.__class__.__name__
          line += actor_name[0].lower()
        else:
          line += " "
      line += "|\n"
      msg += line
    msg += " " + "_" * self.max_largeur + "\n"
    print (msg)

  def getActors(self, with_position=False, only_position=False):
    if only_position:
      return [actor.position for actor in self.actors]
    elif with_position:
      return [[actor.position, actor] for actor in self.actors]

    return self.actors
