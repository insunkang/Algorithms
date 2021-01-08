def solution(clothes):
    answer = 0

    check = {}
    getKey = []
    for i in range(len(clothes)):
        if clothes[i][1] in check:
            check[clothes[i][1]] = check.get(clothes[i][1])+1
        else:            
            getKey.append(clothes[i][1])
            check[clothes[i][1]] = 1
    a = 1
    
    print(getKey)
    for i in range(len(getKey)):
        a *= check[getKey[i]]

    # print(check)
    # print(a+len(clothes))
    answer = a+len(clothes)
    if len(getKey) == 1:
        print(len(clothes)
    else:
        print(a+len(clothes))
    
    return answer
    




solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])

    