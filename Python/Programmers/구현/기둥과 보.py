def check(data):
    for i in data:
        x,y,structure=i
        if structure==0:
            if y==0:
                continue
            if (x-1,y,1) in data or (x,y,1) in data or (x,y-1,0) in data:
                continue
            else:
                return False
        else:
            if (x,y-1,0) in data or (x+1,y-1,0)in data or ((x-1,y,1) in data and (x+1,y,1) in data):
                continue
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for i in build_frame:
        x,y,struct,act=i
        if act==0:
            if (x,y,struct) in answer:
                answer.remove((x,y,struct))
                if(check(answer)):
                    continue
                answer.append((x,y,struct))
        else:
            answer.append((x,y,struct))
            if(check(answer)):
                continue
            answer.remove((x,y,struct))
    answer=sorted(answer,key=lambda x: (x[0],x[1],x[2]))
    
    
    
    return answer