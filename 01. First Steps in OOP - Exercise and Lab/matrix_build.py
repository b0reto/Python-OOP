def build_matrix(rows, cols):
    matrix = []

    for r in range(0, rows):
        matrix.append([0 for c in range(0, cols)])

    print(matrix)

    return matrix

if __name__ == '__main__':
    build_matrix(6, 10)