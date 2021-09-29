n,need=map(int,input().split())

arr=list(map(int,input().split()))
Length=len(arr)

answer=0
i=max(arr)
j=0

while j<=i:
    mid=(i+j)//2
    result=0
    for k in range(len(arr)):
        if arr[k]>mid:
            result+=arr[k]-mid
    if result>=need and answer<mid:
        answer=mid
        j=mid+1
    else:
        i=mid-1
print(answer)


N, M = map(int, input().split())
tree = list(map(int, input().split()))
start, end = 1, max(tree) #이분탐색 검색 범위 설정

while start <= end: #적절한 벌목 높이를 찾는 알고리즘
    mid = (start+end) // 2
    
    log = 0 #벌목된 나무 총합
    for i in tree:
        if i >= mid:
            log += i - mid
    
    #벌목 높이를 이분탐색
    if log >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)