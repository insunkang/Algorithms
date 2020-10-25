# adventure guild

n = int(input())

person = list(map(int, input().split()))

person.sort()
print(person)
result = 0
check = 0
sumP = 0
for i in range(len(person)):
    check+=1
    sump=person[i]
    if sump/check==1:
        result+=1
        check=0
        sumP=0
        print(i)

print(result)


