class Combat():
  continue_combat = True
  nombre_groupes = 0
  JoueursByInit = {}

  def __init__(self, groupes):
    self.nombre_groupes = len(groupes)
    #Determine initiative
    JoueursByInit = []
    for i in range(len(groupes)):
      for j in range(len(groupes[i])):
        joueur = groupes[i][j]
        initiative = joueur.testType("DEX")
        JoueursByInit.append((joueur, initiative, i))

    JoueursByInit = sorted(JoueursByInit, key=lambda tuple: tuple[1], reverse=True)
    self.JoueursByInit = JoueursByInit


  def combat(self):
    i = 0
    while self.checkTeamsAlive() and self.continue_combat:
      joueur = self.JoueursByInit[i][0]
      print(joueur.__str__())
      joueur.tourCombat(self, self.JoueursByInit[i])
      i += 1
      if i == len(self.JoueursByInit):
        self.continue_combat = False
        i = 0

  def getEnnemies(self, joueur_informations):
    ret = []
    for _joueur_informations in self.JoueursByInit:
      if _joueur_informations[2] != joueur_informations[2]:
        ret.append(_joueur_informations)
    return ret

  def checkTeamsAlive(self):
    alive_teams = 0
    for i in range(self.nombre_groupes):
      groupe = filter(lambda joueur: joueur[2] == i, self.JoueursByInit)
      alive_players_by_group = list(filter(lambda joueur: joueur[0].vie >= 0, groupe))
      if (len(alive_players_by_group)):
        alive_teams += 1

    return alive_teams > 1


def checkTeamAlive(groupe):
  for joueur in groupe:
    if joueur.vie > 0:
      return True

  return False
