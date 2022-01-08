from collections import deque


def bfs(boxes, start):
    # x,y,z
    FBLRUD = [[0, 1, 0], [0, -1, 0], [-1, 0, 0],
              [1, 0, 0], [0, 0, -1], [0, 0, 1]]
    que = deque()
    for i in start:
        que.append((i, 0))
    result = 0
    while que:
        pos, day = que.popleft()
        if day > result:
            result = day
        x, y, z = pos
        for i in FBLRUD:

            dx = x+i[0]
            dy = y+i[1]
            dz = z+i[2]

            if dx < 0 or dx >= len(boxes[0][0]) or\
                dy < 0 or dy >= len(boxes[0]) or\
                    dz < 0 or dz >= len(boxes):
                continue
            if boxes[dz][dy][dx] == -1:
                continue
            if boxes[dz][dy][dx] == 1:
                continue
            boxes[dz][dy][dx] = 1
            que.append(((dx, dy, dz), day+1))

    return result


m, n, h = map(int, input().split())

boxes = []

for i in range(h):
    temp = []
    for j in range(n):
        temp.append(list(map(int, input().split())))

    boxes.append(temp)

tomatos = []
for i in range(len(boxes)):
    for j in range(len(boxes[0])):
        for k in range(len(boxes[0][0])):
            if boxes[i][j][k] == 1:
                tomatos.append((k, j, i))
result = bfs(boxes, tomatos)
for i in range(len(boxes)):
    for j in range(len(boxes[0])):
        for k in range(len(boxes[0][0])):
            if boxes[i][j][k] == 0:
                print(-1)
                exit(0)
print(result)
