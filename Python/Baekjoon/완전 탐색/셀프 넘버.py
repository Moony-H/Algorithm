def isNotSelf(n, num):
    # 자릿수 만들기

    arr = []
    temp = num
    while True:
        arr.append(temp % 10)
        if temp < 10:
            break
        temp //= 10

    result = sum(arr)+num
    if result <= 10000 and n[result] == 0:
        n[result] = 1
        isNotSelf(n, result)


n = [0 for i in range(0, 10000+1)]


for i in range(len(n)):
    if n[i] == 1:
        continue
    isNotSelf(n, i)

for i in range(len(n)):
    if n[i] == 0:
        print(i)
