import importlib
from tkinter import Label

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

  def description(self, frame=None):
    print(self.description_str)
    if frame:
      description_label = Label(frame, text=self.description_str)
      return description_label

  def launch(self, scene_name="", player_view=None):
    if scene_name:
      self.current_scene_name = scene_name

    if not self.current_scene_name in self.scenes:
      return False

    module = importlib.import_module("Game.Levels.{}.Scenes.{}".format(self.name, self.current_scene_name))
    module_class = getattr(module, self.current_scene_name)
    self.current_scene = module_class()
    self.current_scene.description()