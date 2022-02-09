def solution(board, skill):
    answer = 0
    change = [[0 for _ in range(len(board[0])+1)]for _ in range(len(board)+1)]
    for i in skill:
        t, r1, c1, r2, c2, d = i
        if t == 1:
            d = -d
        change[r1][c1] += d
        change[r1][c2+1] -= d
        change[r2+1][c1] -= d
        change[r2+1][c2+1] += d
    for i in range(1, len(change[0])):
        change[0][i] += change[0][i-1]
    for i in range(1, len(change)):
        change[i][0] += change[i-1][0]

    for i in range(1, len(change)):
        for j in range(1, len(change[0])):
            change[i][j] = change[i-1][j]+change[i][j-1] + \
                change[i][j]-change[i-1][j-1]

    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] += change[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer
