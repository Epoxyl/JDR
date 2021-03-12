from Game import session

class Session:
  """
  Classe pour manipuler la session
  """
  @staticmethod
  def set(key, value):
    session[key] = value

  @staticmethod
  def get(key):
    if key and key in session.keys():
      return session[key]
    else:
      return None
