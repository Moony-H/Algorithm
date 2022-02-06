import sys
input = sys.stdin.readline
n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
answer = 0
for i in range(n):
    answer = max(answer, arr[i]*(i+1))
print(answer)
