import heapq
n = int(input())

for _ in range(n):
    numbers = int(input())
    q = []
    for i in range(numbers):
        order, number = map(str,input().split(" "))
        if order == "I":
            heapq.heappush(q,int(number))
        elif order =="D" and len(q) > 0:
            if number == "-1":
                heapq.heappop(q)
            else:
                del q[len(q)-1]

    if len(q) == 0:
        print("EMPTY")
    else:
        print(str(max(q))+" "+str(min(q)))
