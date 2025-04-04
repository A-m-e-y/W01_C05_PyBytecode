import numpy as np

def matrix_multiply_numpy(matrix1, matrix2):
  """
  Matrix multiplication using numpy.

  Args:
      matrix1: first matrix.
      matrix2: second matrix.

  Returns:
      result of matrix multiplication.
  """
  return np.dot(matrix1, matrix2).tolist()

if __name__ == '__main__':
  #Example usage with numpy.
  matrix_c = [[1, 2, 3], [4, 5, 6]]
  matrix_d = [[7, 8], [9, 10], [11, 12]]
  
  result_matrix_numpy = matrix_multiply_numpy(matrix_c, matrix_d)
  
  print("Input Matrix 1: ")
  for row in matrix_c:
    print(row)
  print("Input Matrix 2: ")
  for row in matrix_d:
    print(row)
  print("Resultant Matrix using numpy:")
  for row in result_matrix_numpy:
    print(row)