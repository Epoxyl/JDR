from Game.Classes.World.Actors.Actor import Actor

class Meuble(Actor):
  durabilite = 100
  actions_possibles = {
    "laisser": {
      "active": True
    },
    "détruire": {
      "active": False
    }
  }
