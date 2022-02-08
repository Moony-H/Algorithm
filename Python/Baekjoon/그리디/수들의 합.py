s = int(input())
answer = 0
num = 1
while s >= 0:
    s -= num
    num += 1
    answer += 1
print(answer-1)
