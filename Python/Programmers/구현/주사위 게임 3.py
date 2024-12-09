def solution(a, b, c, d):
    answer = 0
    dic={}
    dic[a]=dic.get(a,0)+1
    dic[b]=dic.get(b,0)+1
    dic[c]=dic.get(c,0)+1
    dic[d]=dic.get(d,0)+1
    l=list(dic.items())
    l.sort(key=lambda x:(x[1],x[0]),reverse=True)
    print(l)
    if len(l)==1:
        return 1111*l[0][0]
    if len(l)==2:
        if l[0][1]==2 and l[1][1]==2:
            return (l[0][0]+l[1][0])*abs(l[0][0]-l[1][0])
        else:
            return (l[0][0]*10+l[1][0])**2
    if len(l)==3:
        return l[1][0] * l[2][0]
        
    return l[-1][0]