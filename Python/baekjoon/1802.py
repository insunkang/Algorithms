#000 ->  가운데가 0이면 가운데 기준 왼쪽을 남기고 1이면 오른쪽을 남긴다.
#           왼쪽이 오른쪽의 역순과 같아야하고         오른쪽이 왼쪽의 역순과 같아야 한다.


def check(numbers):
    while len(numbers) != 1:
        a = numbers[:len(numbers)//2]
        b = numbers[len(numbers)//2+1:]
        temp = ""
        for i in range(len(b)-1,-1,-1):
            if b[i] == "0":
                temp += "1"
            else:
                temp += "0"
        if a==temp:
            if numbers[len(numbers)//2] == "0":
                numbers = a
            else:
                numbers = b
            check(numbers)
        else:
            return False
    return True


t = int(input())
for _ in range(t):
    numbers = str(input())
    if check(numbers):
        print("YES")
    else:
        print("NO")


