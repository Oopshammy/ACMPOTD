'''
The approach I used here was first checking whether all the elements in a row are same or not by checking with the first element of each row.
then to check whether the adjacent columns are different or not i checked for each column whether it was same or different to the one below it. 
from this method all the columns' adjency was cecked.
'''


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


