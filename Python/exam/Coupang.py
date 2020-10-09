# import heapq
month = [31,28,31,30,31,30,31,31,30,31,30,31]
def heap(n,customers):
    kiosk = [0] * n

    answer = 0

    return answer
n =3
kiosk = [0] * n
customers = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"] 

customerDate = [] * len(customers)
customerDate[0] = 0
customerTime = [0] * len(customers)
time = 0
for i in range(len(customers)):
    customerTime[i] = int(customers[i].split(" ")[2])

for i in range(1,len(customerDate)):
    a = 0
    if int(customers[i].split(" ")[0].split("/")[0])>int(customers[i].split(" ")[0].split("/")[0]):
        a+=
    else:

    customerDate[i] = int(customers[i].split(" ")[1])

print(customerTime)
