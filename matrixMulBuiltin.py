def matrix_multiply_builtin(matrix1, matrix2):
    """
    Matrix multiplication using Python's built-in functionality.

    Args:
        matrix1: first matrix (list of lists).
        matrix2: second matrix (list of lists).

    Returns:
        result of matrix multiplication as a list of lists.
    """
    # Ensure the number of columns in matrix1 equals the number of rows in matrix2
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Number of columns in matrix1 must equal number of rows in matrix2.")

    # Perform matrix multiplication
    result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*matrix2)] for row in matrix1]
    return result

if __name__ == '__main__':
    # Example usage with larger matrices for increased computation time
    matrix_a = [[i + j * 1000 for i in range(200)] for j in range(200)]
    matrix_b = [[i + j * 1000 for i in range(200)] for j in range(200)]

    result_matrix_builtin = matrix_multiply_builtin(matrix_a, matrix_b)
    
    # print("Input Matrix 1: ")
    # for row in matrix_a:
    #     print(row)
    # print("Input Matrix 2: ")
    # for row in matrix_b:
    #     print(row)
    # print("Resultant Matrix using built-in functionality:")
    # for row in result_matrix_builtin:
    #     print(row)
    print("Matrix multiplication using built-in functionality completed successfully.")
