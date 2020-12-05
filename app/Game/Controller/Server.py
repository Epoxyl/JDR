from functools import partial
import importlib
from Game.IHM.User import User
from Game.Utils.Session import Session

class Server():
  """
  Game server qui lance l'affichage et gère les sessions de jeu
  """
  def __init__(self):
    level_name = "Prison"
    module = importlib.import_module("Game.Levels.{}.{}".format(level_name, level_name))
    module_class = getattr(module, level_name)
    self.current_level = module_class()

    self.user = User(self.current_level)

  def launchGame(self):
    Session.set("User", self.user)
    self.user.launchLevel()

  def event(self, event_name, personnage):
    """
    Action de l'évènement
    :param event_name: Nom de l'évènement
    :param personnage: Personnage ayant fait l'action
    :return:
    """
    callback = partial(self.user.setCharacterInfos, personnage)
    self.user.player_hud.showEvent(event_name, self.current_level.__class__.__name__, callback)