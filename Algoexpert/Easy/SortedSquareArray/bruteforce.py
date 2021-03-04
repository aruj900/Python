def sortedSquaredArray(array):
  sortedSquares = [0 for _ in array]

  for idx in range(len(array)):
      value = array[idx]
      sortedSquares[idx] = value * value

  sortedSquares.sort()
  return sortedSquares
    