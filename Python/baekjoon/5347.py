a = int(input())
questions = []
for _ in range(a):
    b,c = map(int, input().split(" "))
    questions.append([b,c])

for question in questions:
    aGroup = []
    bGroup = []
    for i in range(1,question[0]+1):
        if question[0]%i == 0:

            aGroup.append(i)

            aGroup.append(question[0]//i)
    for i in range(1,question[1]+1):
        if question[1]%i == 0:

            bGroup.append(i)

            bGroup.append(question[1]//i)
    # result = 1
    # for i in aGroup:
    #     if i in bGroup:
    #         result *= i

    print(aGroup,bGroup)
