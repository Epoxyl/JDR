from Game.IHM.UserView import UserView
import importlib

class Server():
  """
  Game server qui lance l'affichage et gère les sessions de jeu
  """
  current_level = None
  player_view = None

  def __init__(self, level_name="Prison"):
    module = importlib.import_module("Game.Levels.{}.{}".format(level_name, level_name))
    module_class = getattr(module, level_name)
    self.current_level = module_class()

    self.player_view = UserView()

  def event(self, event_name):
    self.player_view.showEvent(event_name, self.current_level.__class__.__name__)

  def launchLevel(self):
    self.player_view.showStartLevel(self.current_level)
    self.current_level.launch(player_view=self.player_view)

  def characterHUD(self, personnage, scene):
    character_infos = self.getCharacterInfos(personnage)
    scene_map = self.player_view.getSceneMap(scene.getMap(), personnage)

    self.player_view.showHUD(main_frame=scene_map, right_frame=character_infos)

    self.player_view.loop()

  def getCharacterInfos(self, personnage):
    return self.player_view.getCard("personnage", {"nom":personnage.nom, "age": personnage.age})

  def askQuestion(self, personnage, msg, choix=None, get_choice_str=False, get_object=False):
    if (choix):
      if isinstance(choix, list):
        choix = {i: choix[i] for i in range(0, len(choix))}
      if not isinstance(choix, dict):
        raise Exception("error: wrong ask type")

      choix_str = msg + "\n"

      choix_names = []
      for answer_name, answer in choix.items():
        if isinstance(answer_name, int):
          answer_name = answer
        choix_names.append(answer_name)

      frame_questions = self.player_view.getQuestion(personnage, msg, choix)

