'''
the approach i used was first copying the pattern in a 2d matrix,
and then starting to delete the rows from the beginning which had no stars in them till i reached a row with stars.
then deleting the rows from the end with no stars and stopping once i reached a row with stars. 
doing the same for columns too
'''

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
