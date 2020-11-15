from Game import game_directory, session
from Game.Utils.Session import Session


class Scene():
  """

  """
  hauteur = 1
  largeur = 1
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
    if self.starting_event:
      server = Session.get("Server")
      server.event(self.starting_event)
    print("here")
    Session.get("Server").characterHUD(self.player, self)
    return
    with open(game_directory+"/Levels/Prison/Scenes/{}_description.txt".format(self.name.lower()), 'r') as fp:
      for line in fp:
        if line == "\n":
          input()
        print(line)

    description_str = self.description_str
    for action_name, value in self.events.items():
      description_str += action_name + ": " + value['description'] + "\n"
    chosen_actor_infos = self.chooseActor(asking_actor)
    if chosen_actor_infos:
      chosen_actor: Actor = chosen_actor_infos[1]
      ret = chosen_actor.interaction(self.player)

    self.displayScene()

    return ret

  def loadEmptyMap(self):
    """
    Load the empty map as list
    :return list:
    """
    map_file = open(game_directory+"/Levels/Prison/Scenes/{}_map.txt".format(self.name.lower()))
    lines = map_file.readlines()
    self.largeur = len(lines[0])
    self.hauteur = len(lines)
    return [list(line) for line in lines]

  def getMap(self):
    map = self.loadEmptyMap()
    for actor in self.actors:
      map[actor.position[0]][actor.position[1]] = actor
    return(map)

  def displayScene(self):
    """
    display the scene with actors for User View
    :return:
    """

    # todo: displaySceneForFights
    actors = self.listActors(with_objects=True)
    actors_by_position = {str(actor.position): actor for actor in actors.values()}

    msg = " " + "_" * self.largeur + "\n"
    line = ""
    for y in range(self.hauteur):
      line = "|"
      for x in range(self.largeur):
        if "[{}, {}]".format(x,y) in actors_by_position.keys():
          actor = actors_by_position["[{}, {}]".format(x,y)]
          actor_name = actor.__class__.__name__
          line += actor_name[0].lower()
        else:
          line += " "
      line += "|\n"
      msg += line
    msg += " " + "_" * self.largeur + "\n"
    print (msg)

  def getActors(self, with_position=False, only_position=False):
    if only_position:
      return [actor.position for actor in self.actors]
    elif with_position:
      return [[actor.position, actor] for actor in self.actors]

    return self.actors
