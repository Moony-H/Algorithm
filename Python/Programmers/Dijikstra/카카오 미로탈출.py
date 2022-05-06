from heapq import heappush, heappop
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


print(solution(4, 1, 4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))


# 나의 답

INF = int(1e9)


def solution(n, start, end, roads, traps):
    answer = 0

    que = []
    way = [[INF for _ in range(n+1)]for _ in range(n+1)]
    for i in roads:
        p, q, s = i
        if way[p][q] > s:
            way[p][q] = s
    for i in way:
        print(i)
    for i in range(len(way)):
        way[i][i] = 0
    traps.sort()
    visited = [[False for _ in range(1 << len(traps))]for _ in range(n+1)]
    print(visited)
    heappush(que, (0, start, 0))
    while que:
        payed, node, trapState = heappop(que)
        # 시작시 방문
        print("node: {0}".format(node))
        print("cost: {0}".format(payed))
        if visited[node][trapState]:
            continue

        visited[node][trapState] = True
        actTrap = []
        if node == end:
            return payed
        for i in range(len(traps)):
            if trapState & 1 << i and node == traps[i]:
                # 현재 노드가 트랩이고, 켜져 있을 경우 꺼줌
                trapState &= ~(1 << i)
            elif not (trapState & 1 << i) and node == traps[i]:
                # 현재 노드가 트랩이고, 꺼져 있을 경우 켜줌
                trapState |= 1 << i
                actTrap.append(traps[i])
            elif trapState & 1 << i:
                # 나머지 켜져 있는 Trap 넣기
                actTrap.append(traps[i])
        print("act trap {0}".format(actTrap))
        for i in range(1, n+1):
            if node == i:
                continue
            if node in actTrap and i in actTrap:
                # 둘다 켜져 있는 경우 원래 그래프 사용
                cost = way[node][i]
            elif node in actTrap or i in actTrap:
                # 한쪽만 켜져 있는 경우 반대 그래프 사용
                cost = way[i][node]
            else:
                # 둘다 안켜져 있는 경우 원래 그래프 사용
                cost = way[node][i]
            if cost == INF:
                continue
            heappush(que, (cost+payed, i, trapState))

    return answer


print(solution(4, 1, 4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))
