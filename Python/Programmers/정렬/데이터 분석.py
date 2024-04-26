
def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    keyHash={'code':0,'date':1,'maximum':2,'remain':3}
    extIndex=keyHash[ext]
    sortingIndex=keyHash[sort_by]
    newData=[]
    for i in data:
        if i[extIndex]>=val_ext:
            continue
        newData.append(i)
    return sorted(newData,key=lambda x:x[sortingIndex])