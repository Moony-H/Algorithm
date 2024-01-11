def solution(bandage, health, attacks):
    healTime,healPerSec,addHeal=bandage
    maxH=health
    prevTime=0
    for at,damage in attacks:
        diffTime=at-prevTime-1
        if(diffTime<0):
            diffTime=0
        health+=diffTime*healPerSec
        if((at%healTime!=0) or healTime==1):
            health+=(diffTime//healTime)*addHeal
        if(health>maxH):
            health=maxH
        health-=damage
        if(health<=0):
            return -1
        prevTime=at
    return health