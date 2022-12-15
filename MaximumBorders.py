# Problem title: Maximum borders
# URL: https://www.hackerearth.com/problem/algorithm/maximum-border-9767e14c/

# Retrieves the maximun number of black cells in a matrix (search is per row)
def get_max_blacks(matrix:list):
    max_blacks = 0

    for row in matrix:
        blacks_in_a_row = 0
        prev_cell = ''
        for current in row:
            if prev_cell == '.' and current == '#':
                blacks_in_a_row = 1
            elif current == '#':
                blacks_in_a_row += 1
            prev_cell = current

            if blacks_in_a_row > max_blacks:
                max_blacks = blacks_in_a_row
    return max_blacks

test_cases = int(input())

for t in range(test_cases):
    rows, cols = input().split()
    rows, cols = int(rows), int(cols)
    
    matrix = []
    trans = [['' for j in range(rows)] for i in range(cols)]
    
    # Load matrix from input
    for x in range(rows):
        matrix.append(list(input()))
        # Create Transpose Matrix
        for y, current in enumerate(matrix[x]):
            trans[y][x] = current
    
    max_normal = get_max_blacks(matrix)
    max_trans = get_max_blacks(matrix)
    print(max(max_normal, max_trans))
