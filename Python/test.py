cache=[[int(1e9) for _ in range(152)]for _ in range(152)]


def dfs(cost,problems,ability,goal):
    global cache
    if ability[0]>=goal[0] and ability[1]>=goal[1]:
        return
    
    for i in problems:
        if i[0]<=ability[0] and i[1]<=ability[1]:
            if(ability[0]+i[2]>=152) or (ability[1]+i[3]>=152):
                continue
            if(cache[ability[0]+i[2]][ability[1]+i[3]]<=cost+i[4]):
                continue
            
            else:
                cache[ability[0]+i[2]][ability[1]+i[3]]=cost+i[4]
                dfs(cost+i[4],problems,(ability[0]+i[2],ability[1]+i[3]),goal)



def solution(alp, cop, problems):
    answer = 0
    global cache
    goal=[max([i[0] for i in problems]),max([i[1] for i in problems])]
    problems.append([0,0,1,0,1])
    problems.append([0,0,0,1,1])
    
    dfs(0,problems,(alp,cop),goal)
    print(cache[goal[0]][goal[1]])
    return answer

solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])