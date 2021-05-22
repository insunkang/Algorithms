n, k = map(int, input().split(" "))

time = [0] * 3

result = 0

while True:
    check = ""
    for i in time:
        if i < 10:
            check += "0" + str(i)
        else:
            check += str(i)
    if str(k) in check:
        result += 1
    time[2] += 1
    if time[2] == 60:
        time[2] = 0
        time[1] += 1
    if time[1] == 60:
        time[1] = 0
        time[0] += 1
    if time[0] == n and time[1] == 59 and time[2] == 59:
        Fcheck = ""
        for i in time:
            if i < 10:
                Fcheck += "0" + str(i)
            else:
                Fcheck += str(i)
        if str(k) in Fcheck:
            result += 1
        break

print(result)