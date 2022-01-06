import heapq

INF = int(1e9)


def dijk(n, traps, start, end, graph):
    que = []
    visited = [[False for _ in range(1 << len(traps))]for _ in range(n+1)]
    heapq.heappush(que, (0, start, 0))

    while que:
        cost, now, trapState = heapq.heappop(que)
        print(now)

        if now == end:
            return cost
        if visited[now][trapState] == True:
            continue
        visited[now][trapState] = True

        activatedTraps = []

        for i in range(len(traps)):
            check = 1 << i
            if trapState & check:
                # 현재 위치가 trap인데, state에 놓여 있는 경우(두번 밟은 경우)
                if traps[i] == now:
                    # 꺼줌, 그리고 activatedTraps에는 저장 안함(꺼졌기 때문)
                    trapState &= ~check

                else:
                    activatedTraps.append(traps[i])
            elif traps[i] == now:
                # 현재 위치가 trap인데, state에 없는 경우(trap이 꺼진 상태로 밟은 경우)
                trapState |= check
                activatedTraps.append(traps[i])
        print(activatedTraps)
        for i in range(1, n+1):
            if now == i:
                continue
            if now in activatedTraps and i in activatedTraps:
                # 둘다 trap 발동된 경우.(원래 그래프로 사용)
                if graph[now][i] != INF:
                    heapq.heappush(que, (cost+graph[now][i], i, trapState))
            elif now not in activatedTraps and i not in activatedTraps:
                # 둘다 trap 발동인 아닌 경우.(원래 그래프 사용)
                if graph[now][i] != INF:
                    heapq.heappush(que, (cost+graph[now][i], i, trapState))
            else:
                if graph[i][now] != INF:
                    heapq.heappush(que, (cost+graph[i][now], i, trapState))

    return INF


def solution(n, start, end, roads, traps):
    answer = 0
    graph = [[INF for _ in range(n+1)]for _ in range(n+1)]
    for i in range(n+1):
        graph[i][i] = 0
    for i in roads:
        if graph[i[0]][i[1]] > i[2]:
            graph[i[0]][i[1]] = i[2]

    return dijk(n, traps, start, end, graph)
