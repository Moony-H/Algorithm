import sys
input = sys.stdin.readline
n = int(input())
arr = [i for i in range(2, n+1)]
target = []
for _ in range(n):
    target.append(int(input()))
index = 0
stack = [1]
answer = ['+']
for i in target:

    while (len(stack) == 0 or i > stack[-1]) and len(arr) > index:
        stack.append(arr[index])
        answer.append('+')
        index += 1
    if i == stack[-1]:
        stack.pop()
        answer.append('-')
    else:
        print('NO')
        exit(0)
for i in answer:
    print(i)
