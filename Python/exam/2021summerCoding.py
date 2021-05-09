#1

def solution(code, day, data):
    answer = []
    result = []
    datas = []
    for i in data:
        datas.append(list(map(str,i.split(" "))))
    print(datas)

    for i in datas:
        checkPrice = list(map(str,i[0].split("=")))
        checkCode = list(map(str,i[1].split("=")))
        checkDay = list(map(str,i[2].split("=")))
        # print(checkCode)
        # print(checkDay)
        if checkCode[1] == code and checkDay[1][:8] == day:
            result.append([checkDay[1],checkPrice[1]])
    result.sort()
    print(result)
    for i in result:
        answer.append(int(i[1]))
    print(answer)
    return answer

# solution("012345","20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"])


#2
import heapq
import copy
def solution2(t, r):
    answer = []
    q = []
    time = max(t)
    if len(t) != len(set(t)):
        if time < len(t):
            time += len(t)-time
        for i in range(time + 1):
            # print(i)
            for j in range(len(t)):
                if t[j] == i:
                    heapq.heappush(q, (r[j], j))
            # print(q)
            if len(q) != 0:
                # print("Yes")
                a, tindex = heapq.heappop(q)
                answer.append(tindex)
    else:
        ct = copy.deepcopy(t)
        ct.sort()
        for i in ct:
            answer.append(t.index(i))
    print(answer)
    return answer

solution2([0,1,3,0,4,4,5,6,5]	,[0,1,2,3,4,4,5,5,5])
solution2([7,6,8,1]	,[0,1,2,3])