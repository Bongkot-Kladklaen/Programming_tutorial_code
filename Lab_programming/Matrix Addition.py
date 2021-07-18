row, col = input().split()
numberSum, matrix = [], []

for _ in range(int(row)):
    matrix.append([int(j) for j in input().split()])

for _ in range(int(row)):
    numberSum.append([int(j) for j in input().split()])

for i in range(len(matrix)):
    for j in range(int(col)):
        print(matrix[i][j] + numberSum[i][j], end=" ")
    print()