arr = [300, 60, 10]
t = int(input())
answers = []
for i in arr:
    answers.append(t//i)
    t %= i
if t != 0:
    print(-1)
    exit(0)
print(*answers)
