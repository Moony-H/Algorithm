t = int(input())
for _ in range(t):
    n = int(input())
    cacheUp = [0 for _ in range(n+1)]
    cacheDown = [0 for _ in range(n+1)]

    stickerUp = list(map(int, input().split()))
    stickerDown = list(map(int, input().split()))
    stickerUp.insert(0, 0)
    stickerDown.insert(0, 0)
    cacheUp[1] = stickerUp[1]
    cacheDown[1] = stickerDown[1]
    if n == 1:
        print(max(stickerDown[1], stickerUp[1]))
        continue
    cacheUp[2] = stickerUp[2]+stickerDown[1]
    cacheDown[2] = stickerDown[2]+stickerUp[1]
    for i in range(3, n+1):
        cacheUp[i] = max(cacheDown[i-1]+stickerUp[i],
                         cacheDown[i-2]+stickerUp[i])
        cacheDown[i] = max(cacheUp[i-1]+stickerDown[i],
                           cacheUp[i-2]+stickerDown[i])
    print(max(cacheDown[n], cacheUp[n]))
