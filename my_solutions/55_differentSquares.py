"""
Given a rectangular matrix containing only digits, calculate the number of different 2 × 2 squares in it.

Example

For

matrix = [[1, 2, 1],
          [2, 2, 2],
          [2, 2, 2],
          [1, 2, 3],
          [2, 2, 1]]
the output should be
differentSquares(matrix) = 6.
"""

def differentSquares(matrix):
    submatrix=[]
    for i in range(len(matrix)-1):
        for j in range(len(matrix[0])-1):
            tmp=[matrix[i][j],matrix[i+1][j],matrix[i][j+1],matrix[i+1][j+1]]
            if tmp not in submatrix:
                submatrix.append(tmp)
            
    return len(submatrix)
