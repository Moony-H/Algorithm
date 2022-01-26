from itertools import combinations
arr = []
for _ in range(9):
    arr.append(int(input()))

for i in combinations(arr, 7):
    result = sum(i)
    if result == 100:
        for j in sorted(i):
            print(j)
        exit(0)
