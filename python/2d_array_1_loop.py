def print_matrix(matrix):
    R, C = len(matrix), len(matrix[0])
    row = 0
    col = 0
    while col < C and row < R:
        print(matrix[row][col])
        if col == C-1:
            col = 0
            row += 1
        else:
            col += 1

array = [
    [1,2,3],
]

print_matrix(array)

