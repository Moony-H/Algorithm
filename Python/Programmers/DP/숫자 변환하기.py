def solution(x, y, n):
    answer = 0
    cache=[-1 for _ in range(y+1)]
    cache[x]=0
    for i in range(x,y+1,1):
        results=[]
        minus=i-n
        if minus>=x and cache[minus]!=-1:
            results.append(cache[minus]+1)
        mul2=i//2
        if i%2==0 and mul2>=x and cache[mul2]!=-1:
            results.append(cache[mul2]+1)
        mul3=i//3
        if i%3==0 and mul3>=x and cache[mul3]!=-1:
            results.append(cache[mul3]+1)
        if len(results)>0:
            cache[i]=min(results)
    return cache[y]