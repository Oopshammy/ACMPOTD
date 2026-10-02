n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = input()
    matrix.append(list(row))


while len(matrix) > 0 and '*' not in matrix[0]:
    matrix.pop(0)


while len(matrix) > 0 and '*' not in matrix[-1]:
    matrix.pop()


while len(matrix[0]) > 0 and all(row[0] == '.' for row in matrix):
    for row in matrix:
        row.pop(0)


while len(matrix[0]) > 0 and all(row[-1] == '.' for row in matrix):
    for row in matrix:
        row.pop()


for row in matrix:
    print(''.join(row))