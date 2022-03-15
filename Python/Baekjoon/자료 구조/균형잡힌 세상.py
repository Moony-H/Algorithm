import sys
input = sys.stdin.readline
answer = []
string = input()
while len(string) != 1 and string[0] != '.':
    stack = []
    for i in string:
        if i == '(':
            stack.append(i)
        if i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
                continue
            else:
                stack.append(')')
        if i == '[':
            stack.append(i)
        if i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
                continue
            else:
                stack.append(']')
    if len(stack) == 0:
        answer.append('yes')
    else:
        answer.append('no')
    string = input()
for i in answer:
    print(i)
