def star(arr, x, y, gap):
    if gap == 0:
        arr[y][x] = '*'
        return
    gap //= 3
    star(arr, x, y, gap)
    star(arr, x+gap, y, gap)
    star(arr, x+gap*2, y, gap)

    star(arr, x, y+gap, gap)
    star(arr, x+gap*2, y+gap, gap)

    star(arr, x, y+gap*2, gap)
    star(arr, x+gap, y+gap*2, gap)
    star(arr, x+gap*2, y+gap*2, gap)


n = int(input())
arr = [[' ' for _ in range(n)]for _ in range(n)]
star(arr, 0, 0, n)
for i in arr:
    print(''.join(i))
