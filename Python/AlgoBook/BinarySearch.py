a = int(input())

item = list(map(int,input().split()))

item.sort()
b = int(input())

target = list(map(int,input().split()))


def BS(k,ch):
    if ch==0 or ch==a-1:
        print("no")
        return
    elif item[ch]==k:
        print("yes")
        return
    else:
        BS(k,ch//2)


for i in range(b):
    check=a
    BS(target[i],check)
