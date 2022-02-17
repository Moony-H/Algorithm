arr = list(map(int, input().split()))
cnt = []
for i in arr:
    cnt.append(arr.count(i))
m = max(cnt)
if m == 3:
    print(10000+arr[0]*1000)
elif m == 2:
    i = cnt.index(m)
    print(1000+arr[i]*100)
else:
    print(max(arr)*100)