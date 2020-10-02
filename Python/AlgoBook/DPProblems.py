# 1로 만들기

# x =int(input())

#  앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
# d = [0] * 30001

# while(result != 0):
#     if result%5==0:
#         result=result//5
#     elif result%3==0:
#         result = result // 3
#     elif result % 2 == 0:
#         result = result // 2
#     else:
#         result-=1
#     answer+=1
#
# for i in range(2, x + 1):
# #      현재의 수에서 1을 빼는 경우
#     d[i] = d[i-1] +1
# #       현재의 수가 2로 나누어 떨어지는 경우
#     if i % 2 == 0:
#         d[i] = min(d[i], d[i//2] + 1)
# #     현재의 수가 3으로 나누어 떨어지는 경우
#     if i % 3 == 0:
#         d[i] = min(d[i], d[i//2]+1)
# #     현재의 수가 5로 나누어 떨어지는 경우
#     if i % 5 ==0:
#         d[i] = min(d[i], d[i//5] +1)
# # print(d[x])


#  개미 전사
# n = int(input())
#
# # 모든 식량 정보 입력 받기
# array = list(map(int, input().split()))
# #  앞서 계산된 결과를 저장히기 위한 DP 테이블 초기화
# d = [0]*100
#
# # 다이나믹 프로그래밍(Dynamic Programming) 진행 (바텀업)
# d[0] = array[0]
# d[1] = max(array[0],array[1])
#
# for i in range(2,n):
#     d[i] = max(d[i-1], d[i-2] + array[i])
#
# # 계산된 결과 출력
# print(d[n-1])

# 바닥공사

d = [0]*1000

n = int(input())

d[0] = 1
d[1] = 3
for i in range(2, n):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796

print(d[n-1])
















