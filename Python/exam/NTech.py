# flowers = [[2, 5], [3, 7], [10, 11]]
# ma = 0
# for i in range(len(flowers)):
#     if flowers[i][0]>ma:
#         ma=flowers[i][0]
#     if flowers[i][1]>ma:
#         ma = flowers[i][ 1]
# # print(ma)
# result = 0
# for i in range(1,ma+1):  날짜 동안 하는데
#     count = 0
#     for j in range(len(flowers)): 각 꽃 별로 다 계산
#
#         if flowers[j][0]<=i<flowers[j][1]: 꽃마다 숫자 사이에 날짜가 들어가 있으면
#             count+=1             카운트 해 줘서
#
#     if count > 0:          카운트가 1 이라도 되면
#         result += 1         결과에 포함
#
# print(result)



# 다시 볼거
# histogram= [6, 5, 7, 3, 4, 2]
# answer = 0
# for i in range(len(histogram)-2):
#     for j in range(i+2,len(histogram)):
#         a = min(histogram[i],histogram[j])
#         x = (j-(i+1))*a
#         print(i,j,a,x)
#         answer = max(answer,x)
# print(answer)


#2

n =3

# target = [[0]*n for _ in range(n)]
#
# dx = [-1, 0, 1, 0]
# dy = [0, -1, 0, 1]
#
# def dfs(i,j):
#     for k in range(4):
#         if n>i+dx[k]>=0 and n>j+dy[k]>=0 and target[i+dx[k]][j+dy[k]]==0:
#             dfs()
#
# for i in range(n):
#     for j in range(n):
#         if target[i][j]<
n=7
d=[0]*(n+1)
d[1]=1
d[2]=2

for i in range(3,n+1):
    d[i]=d[i-1]+d[i-2]


print(d[n])
