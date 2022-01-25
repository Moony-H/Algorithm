n = int(input())
if n <= 54:
    for i in range(1, n+1):
        num = i+sum([int(j) for j in str(i)])
        if num == n:
            print(i)
            exit(0)
else:
    for i in range(n-54, n):
        num = i+sum([int(j) for j in str(i)])
        if num == n:
            print(i)
            exit(0)
print(0)
