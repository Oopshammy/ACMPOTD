n, m = map(int, input().split())

matrix = []

for i in range(n):
    row = list(map(int, input()))
    matrix.append(row)

samerow= True
for i in range(n):
    for j in range(m):
        if matrix[i][0] != matrix[i][j]:
            samerow=False
            break
    if not samerow:
        break    

samecol=True

for i in range(n-1):
    if matrix[i][0]==matrix[i+1][0]:
        samecol=False
        break

print("YES" if samecol and samerow else "NO")


