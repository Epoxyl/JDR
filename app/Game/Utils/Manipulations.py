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