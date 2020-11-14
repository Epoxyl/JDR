from Game.IHM.UserView import *

def characterHUD(personnage, scene):
  character_infos = getCharacterInfos(personnage)
  scene_map = getSceneMap(scene.displayScene())

  scene_map.pack()
  character_infos.pack()
  showHUD(right_frame=character_infos)

def getCharacterInfos(personnage):
  return getCard("personnage", {"nom":personnage.nom, "age": personnage.age})