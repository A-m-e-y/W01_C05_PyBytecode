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
  matrix_a = [[i + j * 1000 for i in range(200)] for j in range(200)]
  matrix_b = [[i + j * 1000 for i in range(200)] for j in range(200)]

  result_matrix_numpy = matrix_multiply_numpy(matrix_a, matrix_b)
  
 #  print("Input Matrix 1: ")
 #  for row in matrix_a:
 #    print(row)
 #  print("Input Matrix 2: ")
 #  for row in matrix_b:
 #    print(row)
 #  print("Resultant Matrix using numpy:")
 #  for row in result_matrix_numpy:
 #    print(row)
  print("Matrix multiplication using NumPy completed successfully.")