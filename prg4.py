def multiply_matrices(matrix_a, matrix_b):


    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])

    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    # columns of A must equal rows of B
    if cols_a != rows_b:
        print(f"Error: Cannot multiply matrices. "
              f"Matrix A columns ({cols_a})" f" must match Matrix B rows ({rows_b}).")
        return None

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]


    # Perform matrix multipl
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def print_matrix(matrix, name):

    if matrix is None:
        return
    print(f"\n{name}:")
    for row in matrix:
        print(row)


def inp_matrix():
    # Input matrix dimensions
    m = int(input("Enter the number of rows (m): "))
    n = int(input("Enter the number of columns (n): "))

    matrix = []
    print(f"Enter the elements row by row ({n} elements per row):")


    for i in range(m):
        row = list(map(int, input(f"Row {i + 1}: ").split()))

        while len(row) != n:
            print(f"Error: Please enter exactly {n} elements.")
            row = list(map(int, input(f"Row {i + 1}: ").split()))
        matrix.append(row)


    print("\nThe resulting matrix is:")
    for row in matrix:
        print(*(f"{elem:4}" for elem in row))

    return matrix