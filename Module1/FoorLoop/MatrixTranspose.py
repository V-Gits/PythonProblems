MATRIX = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print("\nOrginal Matrix: ")
for row in MATRIX:
    print(row)

TRANSPOSE_MATRIX = []
for i in range(len(MATRIX)):
    ROW = []
    for j in range(len(MATRIX[i])):
        ROW.append(MATRIX[j][i])
    TRANSPOSE_MATRIX.append(ROW)
print("\nTRANSPOSE MATRIX: ")
for row in TRANSPOSE_MATRIX:
    print(row)