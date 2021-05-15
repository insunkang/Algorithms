from itertools import combinations

def solution(n, capacity, files):
    answer = 0
    if min(files) > capacity:
        return 0
    ncheck = 0
    while len(files)>0 and ncheck !=n:
        # if ncheck == n:
        #     break
        # if len(files) ==0:
        #     break
        for i in range(len(files),-1,-1):
            sumcheck = dict()
            key = []
            for j in range(i,len(files)):
                checkList = files[:i]
                checkList.append(files[j])
                if sum(checkList) <= capacity:
                    if sumcheck.get(sum(checkList)) is None:
                        key.append(sum(checkList))
                        sumcheck[sum(checkList)] = [checkList]
                    else:
                        sumcheck[sum(checkList)].append(checkList)
            if len(key) != 0:
                key.sort(reverse=True)

                print("sumcheck=",sumcheck)
                keyValue = sumcheck.get(key[0])
                print(keyValue)
                answer += len(keyValue[0])
                for j in keyValue[0]:
                    files.remove(j)
                ncheck += 1
                # print(answer)
                # print(ncheck)
                break
    print(answer)







    return answer

# solution(2,5,[1,2,3,4,5])
# solution(2,5,[1,1,1,1,1])
solution(2,3,[2,2,2,2,2])