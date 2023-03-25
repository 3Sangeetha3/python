#a program to find the transpose of the given matrix

matrix = [[1,2,3,4],
          [5,6,7,8],
          [9,10,11,12]]
print("matrix:",matrix)
result = [[0,0,0],
          [0,0,0],
          [0,0,0],
          [0,0,0]]
for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        result[j][i] = matrix[i][j]
print("transpose of the matrix:",result)