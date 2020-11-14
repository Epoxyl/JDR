import importlib

from Game.Classes.Personnage import Personnage
from Game.Classes.World.Scene import Scene

class level():
  name = ""
  description_str = ""
  scenes = {}
  current_scene: Scene = None
  current_scene_name = ""

  def __init__(self, name="Prison"):
    self.name = name
    self.description()

  def description(self):
    print(self.description_str)


  def launch(self, scene_name=""):
    if scene_name:
      self.current_scene_name = scene_name

    if not self.current_scene_name in self.scenes:
      return False

    print("######### {} - {} ###############".format(self.name, self.current_scene_name))
    module = importlib.import_module("Game.Levels.{}.Scenes.{}".format(self.name, self.current_scene_name))
    module_class = getattr(module, self.current_scene_name)
    self.current_scene = module_class()
    self.current_scene.description()