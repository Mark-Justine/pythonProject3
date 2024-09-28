def transpose_matrices(matA, matB):
    try:
        row_A = len(matA)
        column_A = len(matA[0])
        row_B = len(matB)
        column_B = len(matB[0])
        transposed_A = [[0 for _ in range(row_A)] for _ in range(column_A)]
        for i in range(row_A):
            for j in range(column_A):
                transposed_A[j][i] = matA[i][j]

        transposed_B = [[0 for _ in range(row_B)] for _ in range(column_B)]
        for i in range(row_B):
            for j in range(column_B):
                transposed_B[j][i] = matB[i][j]

        return transposed_A, transposed_B
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None, None