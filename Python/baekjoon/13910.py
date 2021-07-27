import sys
import copy
input = sys.stdin.readline

n,m = map(int, input().split(" "))

woak = list(map(int, input().split(" ")))

availableWoak = copy.deepcopy(woak)

for i in range(len(woak)):
    for j in range(i+1,len(woak)):
        if woak[i]+woak[j] not in availableWoak:
            availableWoak.append(woak[i]+woak[j])

print(availableWoak)


tempnow = []


def find(now, woaks, num, target):
    print("before", tempnow)
    if target in now:
        print(num)
        return num
    elif len(now) == 0:
        return -1
    else:
        for i in now:
            for j in woaks:
                if i+j <= target and i+j not in tempnow:
                    tempnow.append(i+j)
                    print("after", tempnow)
        find(tempnow,woaks,num+1,target)




print(find(availableWoak,availableWoak,0,n))



