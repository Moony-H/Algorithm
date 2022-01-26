n = int(input())
arr = []

for _ in range(n):
    arr.append(tuple(map(int, input().split())))

rank = [1 for _ in range(n)]

for i in range(len(arr)):
    for j in range(len(arr)):
        if i == j:
            continue
        if arr[i][0] < arr[j][0] and arr[i][1] < arr[j][1]:
            rank[i] += 1

for i in rank:
    print(i, end=' ')
