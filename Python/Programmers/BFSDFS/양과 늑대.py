import sys
sys.setrecursionlimit(100)


def dfs(count, sheep, wolf, info, tree, start, candidate):

    candidate = candidate & ~(1 << start)

    if info[start] == 1:
        wolf += 1
    else:
        sheep += 1

    if wolf >= sheep:
        return
    count[0] = max(count[0], sheep)

    for i in tree[start]:

        candidate |= 1 << i

    bit = 0b1
    index = 0

    while candidate >= bit << index:

        if candidate & (bit << index):

            dfs(count, sheep, wolf, info, tree, index, candidate)
        index += 1
    return


def solution(info, edges):
    answer = 0
    tree = [[] for _ in info]
    for s, e in edges:
        tree[s].append(e)

    count = [0]
    dfs(count, 0, 0, info, tree, 0, 0b0)

    return count[0]
