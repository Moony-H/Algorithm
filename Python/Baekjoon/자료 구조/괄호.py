answer = []
n = int(input())
change = {'(': 0, ')': 1}
for _ in range(n):
    string = input()
    stack = []
    for i in string:
        temp = change[i]
        stack.append(temp)
        if len(stack) < 2:
            continue
        if stack[-1] == 1 and stack[-2] == 0:
            stack.pop()
            stack.pop()
    if len(stack) == 0:
        answer.append('YES')
    else:
        answer.append('NO')

for i in answer:
    print(i)
