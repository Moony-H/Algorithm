def clean(pos, table):  # 현재 위치 청소 및 답 +1
    global answer
    answer += 1
    x, y = pos
    table[y][x] = 2


def turn(dir):  # 방향 돌리기
    dir -= 1
    if dir == -1:
        dir = 3
    return dir


#위, 오른, 아래, 왼 [전진, 후진] [x,y]
URDL = [[[0, -1], [0, 1]], [[1, 0], [-1, 0]],
        [[0, 1], [0, -1]], [[-1, 0], [1, 0]]]
answer = 0
height, width = map(int, input().split())

y, x, dir = map(int, input().split())

table = []

for i in range(height):
    table.append(list(map(int, input().split())))

# 사방으로 벽이 막혀 있기 때문에 index out of range가 나지 않는다.

while True:
    if table[y][x] == 0:
        # 청소가 안되어 있을 때
        clean((x, y), table)

    allClean = True  # 모두 청소 되어 있나?(또는 벽과 청소했던 곳이 사방에 있나?)
    for i in range(4):
        ddir = turn(dir)  # 임시로 돌려봄
        dx = x+URDL[ddir][0][0]  # x에 [방향][전진][x] 더하기
        dy = y+URDL[ddir][0][1]  # y에 [방향][전진][y] 더하기

        if table[dy][dx] == 1 or table[dy][dx] == 2:  # 벽이거나 청소를 이미 한 곳
            dir = ddir
            continue
        allClean = False  # 청소 안되어 있는 곳 찾음
        dir = ddir  # 임시로 돌리지 말고 ㄹㅇ로 돌리기.
        x = dx
        y = dy
        break
    if allClean:  # 모두 청소? (또는 막혀있나?)
        dx = x+URDL[dir][1][0]  # 후진 방향
        dy = y+URDL[dir][1][1]  # 후진 방향

        if table[dy][dx] == 1:  # 뒤가 막혀 있다면
            break
        else:  # 아니면 후진
            x = dx
            y = dy
print(answer)
