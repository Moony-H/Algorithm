n = input()
temp = n
count = 0
while True:
    if len(temp) < 2:
        temp = '0'+temp
    a = int(temp[0])+int(temp[1])
    temp = temp[-1]+str(a)[-1]
    count += 1
    if int(temp) == int(n):
        break
print(count)
