import numpy as np
# Task a)
# Implement a method, calculating a base change matrix.
# Input: lists sourceBase and targetBase - lists of vectors (e.g. [np.array([1, 2, 3]), np.array([2, 0, 1]), ...])
# Output: Matrix A - a 2D np.array, with len(sourceBase) x len(targetBase) entries
def changeBase(sourceBase: list, targetBase: list) -> np.array:
  A = np.array(sourceBase).T
  B = np.array(targetBase).T
  B_inverted = np.linalg.inv(B)

  return np.dot(B_inverted,A)

# Task b)
# Implement a method, checking if a subBase spans a Subvectorspace of the space spanned by the given base
# Input: lists sourceBase and subSpace - lists of vectors (e.g. [np.array([1, 2, 3]), np.array([2, 0, 1]), ...])
# Output: bool
def spansSubSpace(sourceBase: list, subBase: list) -> bool:
  B = np.matrix(sourceBase)
  S = np.matrix(subBase)
  rankB = np.linalg.matrix_rank(B)
  union_matrix = np.concatenate((B, S))

  if (np.linalg.matrix_rank(union_matrix) == rankB):
      return True
  return False
