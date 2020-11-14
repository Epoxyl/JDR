def array_intersect(array1, array2):
  """
  Intersection d'arrays
  :param array1:
  :param array2:
  :return:
  """
  if not isinstance(array1, list):
    array1 = [array1]
  if not isinstance(array2, list):
    array2 = [array2]

  inter = [value for value in array1 if value in array2]
  return inter

def dict_merge(dict1, dict2):
  if not isinstance(dict1, dict):
    dict1 = [dict1]
  if not isinstance(dict2, dict):
    dict2 = [dict2]

  return {**dict1, **dict2}

def RepresentsInt(s):
  try:
    int(s)
    return True
  except ValueError:
    return False