def matrix_chain_multiplication(matrices):
    n = len(matrices)
    
       dimensions = [[0] * n for _ in range(n)]
    parenthesization = [[0] * n for _ in range(n)]
    
   
    for i in range(1, n):
        dimensions[i][i] = 0
    
   
    for chain_length in range(2, n):
        for i in range(1, n - chain_length + 1):
            j = i + chain_length - 1
            dimensions[i][j] = float('inf')
            for k in range(i, j):
                cost = dimensions[i][k] + dimensions[k+1][j] + matrices[i-1][0] * matrices[k][1] * matrices[j][1]
                if cost < dimensions[i][j]:
                    dimensions[i][j] = cost
                    parenthesization[i][j] = k
    
    
    def print_optimal_parenthesization(i, j):
        if i == j:
            print(f'M{str(i)}', end='')
        else:
            print("(", end='')
            print_optimal_parenthesization(i, parenthesization[i][j])
            print_optimal_parenthesization(parenthesization[i][j] + 1, j)
            print(")", end='')

    print("Optimal Parenthesization: ", end='')
    print_optimal_parenthesization(1, n - 1)
    print("\nMinimum Scalar Multiplications:", dimensions[1][n - 1])


matrices = [(2, 3), (3, 4), (4, 2)]
matrix_chain_multiplication(matrices)
