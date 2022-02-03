n = int(input())
change = 1000-n
answer = 0
yen = [500, 100, 50, 10, 5, 1]
for i in yen:
    answer += change//i
    change %= i
print(answer)
