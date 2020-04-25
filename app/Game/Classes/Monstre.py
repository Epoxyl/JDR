from abc import ABC, abstractmethod

class Monstre(ABC):
  life = 0
  equipement = {
  }

  def __init__(self):
    print("I am born !")

  @abstractmethod
  def attaque(self, personnage):
    """

    :param personnage:
    :return:
    """
    personnage.takeDamage()