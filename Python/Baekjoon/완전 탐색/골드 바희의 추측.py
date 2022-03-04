arr = [1 for _ in range(10001)]
prime = []
for i in range(2, 10001):
    if arr[i] == 0:
        continue

    for j in range(i*2, 10001, i):
        arr[j] = 0
#prime = [i for i in range(len(arr)) if arr[i] != 0]
t = int(input())
for _ in range(t):
    n = int(input())
    a = n//2
    b = a
    while True:
        if arr[a] == 1 and arr[b] == 1:
            print(a, b, sep=' ')
            break
        a -= 1
        b += 1