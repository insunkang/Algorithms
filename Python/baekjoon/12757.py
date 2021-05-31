from bisect import bisect_left
import sys
input = sys.stdin.readline
# a = [1,2,3,5,6,7]
# print(bisect_left(a,4))
# print(bisect_right(a,4))
# print(bisect_right(a,5))

n, m, k = map(int,input().split(" "))

keys = []
jbnu = {}

for _ in range(n):
    a, b = map(int, input().split(" "))
    nowkey = bisect_left(keys, a)
    keys.insert(nowkey,a)
    jbnu[a] = b


# keys.sort()
# print(keys)
# print(jbnu)
result = []
for _ in range(m):
    inputs = list(map(int,input().split(" ")))
    if inputs[0] == 1:
        bikey = bisect_left(keys, inputs[1])
        keys.insert(bikey,inputs[1])
        jbnu[inputs[1]] = inputs[2]
        # keys.sort()
    else: # inputs[0] == 2, 3
        if inputs[1] in keys:
            if inputs[0] == 3:
                result.append(jbnu[inputs[1]])
                # print(jbnu[inputs[1]])
            else:
                jbnu[inputs[1]] = inputs[2]
        else:
            index = bisect_left(keys, inputs[1])
            if index == len(keys):
                if abs(inputs[1]-keys[len(keys)-1]) <= k:
                    if inputs[0] == 3:
                        result.append(jbnu[keys[len(keys)-1]])
                        # print(jbnu[keys[len(keys)-1]])
                    else:
                        jbnu[keys[len(keys) - 1]] = inputs[2]
                else:
                    if inputs[0] == 3:
                        result.append(-1)
                        # print("-1")
            elif index == 0:
                if abs(inputs[1]-keys[0]) <= k:
                    if inputs[0] == 3:
                        result.append(jbnu[keys[0]])
                        # print(jbnu[keys[0]])
                    else:
                        jbnu[keys[0]] = inputs[2]
                else:
                    if inputs[0] == 3:
                        result.append(-1)
                        # print(-1)
            else:
                a = keys[index-1]
                b = keys[index]
                am = abs(a-inputs[1])
                bm = abs(b-inputs[1])
                if am <= k and bm <=k:
                    if am > bm:
                        if inputs[0] == 3:
                            result.append(jbnu[b])
                            # print(jbnu[b])
                        else:
                            jbnu[b] = inputs[2]
                    elif bm > am:
                        if inputs[0] == 3:
                            result.append(jbnu[a])
                            # print(jbnu[a])
                        else:
                            jbnu[a] = inputs[2]
                    elif am == bm:
                        if inputs[0] == 3:
                            result.append("?")
                            # print("?")
                elif am <= k and bm > k:
                    if inputs[0] == 3:
                        result.append(jbnu[a])
                        # print(jbnu[a])
                    else:
                        jbnu[a] = inputs[2]
                elif am > k and bm <= k:
                    if inputs[0] == 3:
                        result.append(jbnu[b])
                        # print(jbnu[b])
                    else:
                        jbnu[b] = inputs[2]
                else:
                    if inputs[0] == 3:
                        result.append(-1)
                        # print("-1")

for i in result:
    print(i)