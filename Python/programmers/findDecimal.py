from itertools import combinations, permutations
def solution(number):
    answer = []
    for i in range(1,len(number)+1):
        test = list(number)
        find = permutations(test,i)

        for j in find:
            j = list(j)
            # print(j)
            while j[0] == "0" and len(j)>1:
                del(j[0])
            a = "".join(j)
            check = 0
            if int(a) == 1 or int(a) == 0:
                continue
            for k in range(2,int(a)):
                if int(a)%k == 0:
                    check += 1
                    break
            if check == 0 and a not in answer:
                answer.append(a)
    return len(answer)