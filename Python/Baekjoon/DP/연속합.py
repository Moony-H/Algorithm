n = int(input())

numbers = list(map(int, input().split()))
cache = [0 for _ in range(n)]
cache[0] = numbers[0]

for i in range(1, len(numbers)):
    cache[i] = max(numbers[i], cache[i-1] + numbers[i])

print(max(cache))
