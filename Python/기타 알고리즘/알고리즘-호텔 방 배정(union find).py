import sys
sys.setrecursionlimit(10000000)



def emptyRoom(m, room_list):
    if  m not in room_list:
        room_list[m]=m+1
        return m
    else:
        temp=emptyRoom(room_list[m],room_list)
        room_list[m]=temp+1
        return temp





def solution(k, room_number):
    room_list=dict()
    answer = []
    
    for j in room_number:
        temp=emptyRoom(j,room_list)
        answer.append(temp)
    return answer