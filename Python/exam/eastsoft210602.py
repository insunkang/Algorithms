from collections import deque
from itertools import combinations


def solution(p, s):
    answer = 0
    q = deque()
    for i in range(len(s)):
        q.append(s[i])
        if len(q) == len(p):
            if "".join(q) == p:
                q = deque()
            else:
                q.popleft()
                answer += 1
    answer += len(q)
    if answer == len(s):
        print(-1)
    else:
        print(1)
        if answer > 2:
            realanswer = answer
            checklist = [i for i in range(len(s))]
            for i in range(answer-2,answer):
                print(1)
                combi = list(combinations(checklist,i))
                ziplist = []
                for j in combi:
                    print(1)
                    for k in range(len(s)):
                        if s[k] not in j:
                            ziplist.append(s[k])
                        q = deque()
                        yes = 1
                        for l in range(len(ziplist)):
                            if len(q) == 0:
                                q.append(ziplist[l])
                            elif len(q) == len(p):
                                if "".join(q) == p:
                                    q = deque()
                                else:
                                    yes = 0
                                    break
                        if yes == 0:
                            break
            answer = realanswer
            print(answer)
        else:
            print(answer)


solution("101","10100010101101100")
# solution("110","110110110")
# solution("000","00000000")
# solution("00","1111111")