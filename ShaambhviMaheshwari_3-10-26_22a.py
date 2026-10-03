n= int(input())

array = list(map(int, input().split()))

arr = list(set(array))

arr.sort()

print(arr[1] if len(arr)>1 else 'NO')






