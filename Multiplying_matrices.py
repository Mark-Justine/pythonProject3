def multiplying_matrices(matA, matB):
    row_A = len(matA)
    column_A = len(matA[0])
    row_B = len(matB)
    column_B = len(matB[0])

    if column_A != row_B:
        raise ValueError("The number of columns in matrix_A must equal the number of rows in matrix_B.")
    result = [[0 for _ in range(column_B)] for _ in range(row_A)]

    for i in range(row_A):
        for j in range(column_B):
            for k in range(column_A):
                result[i][j] += int(matA[i][k]) * int(matB[k][j])

    return result