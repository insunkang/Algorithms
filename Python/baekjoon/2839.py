# import sys

# input = sys.stdin.readline

# n = int(input())

# result = 0

# while n >= 0:
#     if n % 5 == 0:
#         result += n//5
#         break
#     n -= 3
#     result += 1
#     if n < 3:
#         result = -1
        

# print(result)


sugar = int(input())

bag = 0
while sugar >= 0 :
    if sugar % 5 == 0 :  # 5의 배수이면
        bag += (sugar // 5)  # 5로 나눈 몫을 구해야 정수가 됨
        print(bag)
        break
    sugar -= 3  
    bag += 1  # 5의 배수가 될 때까지 설탕-3, 봉지+1
else :
    print(-1)