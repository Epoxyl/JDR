from Game.Classes.Level import level


class Prison(level):
  current_scene_name = "Chambre"
  description_str = "Level : La prison d'Arkatraz"

  scenes = {
    "Chambre": {
      "active": True,
    }
  }