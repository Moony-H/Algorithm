def fac(x):
    if(x==0):
        return 1
    answer=1
    for i in range(1,x+1):
        answer*=i
    return answer
def comb(x):
    return fac(x)/(fac(x-2)*2)

def solution(weights):
    answer=0
    #비둘기 집의 원리
    humans=[0 for _ in range(1001)]
    
    for i in weights:
        humans[i]+=1
    
    for i in range(len(humans)):
        if(humans[i]==0):
            continue
        if(humans[i]>1):
            res=comb(humans[i])
            answer+=res
        if (i*2<=1000 and humans[i*2]!=0):
            answer+=humans[i]*humans[i*2]
            
        n=i*3/2
        if n<=1000 and int(n)==n and humans[int(n)]!=0:
            answer+=humans[i]*humans[int(n)]
        
        n=i*4/3
        if n<=1000 and int(n)==n and humans[int(n)]!=0:
            answer+=humans[i]*humans[int(n)]
    
    return answer