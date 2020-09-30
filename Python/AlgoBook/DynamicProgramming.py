# 피보나치 수열 소스코드 (재귀적)
#  한 번 계산된 결과를 메모제이션(Memoization)하기 위한 리스트 초기화
d = [0]*100

def fibo(x):
    # 종료 조건(1 혹은 2 일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    # 아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

# print(fibo(99))


def pibo(x):
    print('f(' + str(x)+')', end=' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    return  d[x]
# pibo(6)

#  이처럼 재귀함수를 이용하여 DP를 하는 벙범은 큰 문제를 해결하기 위해 작은 문제를 호출한다고 하여 Top-Down 방식
#  반면에 단순히 반복문을 이용하여 소스코드를 작성하는 경우 작은 문제부터 차근차근 답을 도출한다고 하여 Bottom-up 방식

d[1]=1
d[2]=2
n=99
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

# print(d[n])

