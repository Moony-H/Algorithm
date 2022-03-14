n = int(input())
distance = list(map(int, input().split()))
gasstation = list(map(int, input().split()))

gas = gasstation[0]
answer = gas*distance[0]
for i in range(1, n-1):
    if gas > gasstation[i]:
        gas = gasstation[i]
    answer += gas*distance[i]

print(answer)
