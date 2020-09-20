# print("'Hello'")
# print('"Hello"')
# print('"!@#$%^&*()"')
# print('"C:\Download\hello.cpp"')
# import io, sys
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf8')
# a = "\u250C\u252C\u2510"
# b = "\u251C\u253C\u2524"
# c = "\u2514\u2534\u2518"
# print(a)
# print(b)
# print(c)
# a = float(input())
# print("%f" % a)
# a,b=map(int,input().split())
#
#
# print(a,b)

# a,b = map(str, input().split())
#
# print(b,a)

# a = float(input())
#
# print("%.2f" %a)

# a = int(input())
#
# print(a,a,a)
#
# a,b,c=map(int,input().split("."))
#
# # print(a,b,c)
# print("%04d" % a, end=".")
# print("%02d" % b, end=".")
# print("%02d" % c)

# a,b = map(str,input().split("-"))
#
# print(a,end="")
# print(b)

# a,b = map(str,input().split("."))
# a = str(input());
#
# for i in range(len(a)):
#     b = a[i]
#     print("'"+b+"'")


# a = input()
#
# print("["+a[0]+"0000"+"]")
# print("["+a[1]+"000"+"]")
# print("["+a[2]+"00"+"]")
# print("["+a[3]+"0"+"]")
# print("["+a[4]+"]")

# a,b,c = map(str, input().split(":"))
# if b=="00":
#     print("0")
# else:
#     print(b)
#


# a,b,c = map(str, input().split("."))
#
# print(c,end="-")
# print(b,end="-")
# print(a)

# a = float(input())
# print("%.11lf" %a)

# a = int(input())
#
# # print("%o" %a)
# print("%X" %a)

# 8진수 입력
# a = input()
# n= int(a,8)
# print(n)

# 16진수 8진수
# a = input()
# n = int(a, 16)
#
# print("%o" %n)
# 아스키
# a = input()
#
# c = ord(a)
#
# print(c)

# a = int(input())
#
# c = chr(a)
#
# print(c)

# a,b = map(int,input().split())
#
# print(a+b)
# a = int(input())
#
# print(-a)

# a = input()
# a = ord(a)
# a= a+1
#
# print(chr(a))

# a,b =map(int,input().split())
#
# a=a//b
#
# print(a)

# a,b =map(int,input().split())
#
# a=a%b
#
# print(a)

# print(int(input())+1)

# a,b = map(int, input().split())
# c= a/b
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)
# print("%.2f" %c)

# a,b,c = map(int, input().split())
# sum = a+b+c
# avg = sum/3
# print(sum)
# print("%.1f" %avg)

# a,b = map(int, input().split())
#
# print(a*1<<b)

# a,b = map(int, input().split())
#
# print(int(a>b))


# a,b = map(int, input().split())
#
# print(int(a==b))

# a,b = map(int, input().split())
#
# if a==b:
#     print(0)
# else:
#     print(1)

# a= int(input())
#
# if a==1:
#     print(0)
# else:
#     print(1)

# a,b= map(int,input().split())
#
# if a==1 and b==1:
#     print(1)
# else:
#     print(0)

# a,b= map(int,input().split())
#
# if a==1 or b==1:
#     print(1)
# else:
#     print(0)


# a,b= map(int,input().split())
#
# if a!=b:
#     print(1)
# else:
#     print(0)
#
# a,b= map(int,input().split())
#
# if a==0 and b==0:
#     print(1)
# else:
#     print(0)


# a,b= map(int,input().split())
# #
# # if a==0 and b==0:
# #     print(1)
# # else:
# #     print(0)

# a = int(input())
#
# a = ~a
#
# print(a)

# a,b = map(int, input().split())
#
# c = a&b
#
# print(c)

# a,b = map(int, input().split())
#
# c = a|b
#
# print(c)

# a,b = map(int, input().split())
#
# c = a^b
#
# print(c)

# a,b = map(int, input().split())
#
# if a>b:
#     print(a)
# else:
#     print(b)

# a,b,c = map(int, input().split())
#
# print(min(a,b,c))
# a = list(map(int, input().split()))
#
# for i in range(len(a)):
#     if a[i]%2==0:
#         print(a[i])

# a = list(map(int, input().split()))
#
# for i in range(len(a)):
#     if a[i]%2==0:
#         print("even")
#     else:
#         print("odd")

# a = int(input())
#
# if a>0:
#     print("plus")
# else:
#     print("minus")
#
# if a%2==0:
#     print("even")
# else:
#     print("odd")

# a = int(input())
#
# if a>=90:
#     print("A")
# elif a>=70 :
#     print("B")
#
# elif a>=40:
#     print("C")
# else:
#     print("D")
# a = input()
#
# if a=="A":
#     print("best!!!")
# elif a=="B" :
#     print("good!!")
#
# elif a=="C":
#     print("run!")
# elif a=="D":
#     print("slowly~")
# else:
#     print("what?")

# a = int(input())
#
# if a==12 or a== 1 or a== 2:
#     print("winter")
# elif a>=3 and a<= 5 :
#     print("spring")
#
# elif a>=6 and a<= 8:
#     print("summer")
# else :
#     print("fall")

# a = list(map(int,input().split()))
#
# for i in range(len(a)):
#     if a[i]==0:
#         break
#     else:
#         print(a[i])
#
# a = int(input())
# b = list(map(int,input().split()))
#
#
# for i in range(a):
#
#     print(b[i])


# a = list(map(int,input().split()))
#
# i = 0;
# while(a[i]!=0):
#     print(a[i])
#     i=i+1
# a = input()
#
# i = "a"
# while(True):
#     if i==a:
#         print(i)
#         break
#     else:
#         print(i)
#         i=chr(ord(i)+1)
# a = int(input())
#
# i=0
# for k in range(a+1):
#     if k%2==0:
#         i=i+k
#
#
# print(i)

# a = list(map(str,input().split()))
#
#
# for k in range(len(a)):
#     if a[k]!="q":
#         print(a[k])
#     else:
#         print("q")
#         break

# a = int(input())
#
# i=0
# sum=0
# while(True):
#    sum=sum+i
#    if sum>=a:
#        print(i)
#        break
#    else:
#        i=i+1


# a,b = map(int, input().split())
#
# for m in range(1,a+1):
#     for n in range(1,b+1):
#         print(m,n)

# x=str(input())
#
#
# a=int(x,16)
#
# for m in range(1,16):
#     b= a*m
#     print(x, end="")
#     print("*",end="")
#     print("%X" %m, end="")
#     print("=", end="")
#     print("%X" %b)

# a = int(input())
#
# for i in range(1,a+1):
#     if i%3==0:
#         print("X")
#     else:
#         print(i)
# a,b,c = map(int, input().split())
# sum=0
# for i in range(a):
#     for j in range(b):
#         for k in range(c):
#             sum=sum+1
#             print(i,j,k)
#
#
# print(sum)

# a = list(map(int, input().split()))
#
# to = float(1/8/1024/1024)
# for i in range(len(a)):
#
#      to=to*a[i]
#
#
# print("%.1f" %to,"MB")
# a = list(map(int, input().split()))
#
# to = float(1/8/1024/1024)
# for i in range(len(a)):
#
#      to=to*a[i]
#
#
# print("%.2f" %to,"MB")

# a = int(input())
# i=0
# sum=0
# while(True):
#     sum=sum+i
#     if(sum>=a):
#         print(sum)
#         break
#     else:
#         i=i+1
#
# a = int(input())
# i=1
#
# while(True):
#
#     if(i==a):
#         print(a)
#         break
#     elif(i%3!=0):
#         print(i)
#     i = i + 1


# a = list(map(int,input().split()))
#
# res = a[1]*(a[2]-1)+a[0]
#
# print(res)
#
# a = list(map(int,input().split()))
#
# res = a[1]**(a[2]-1)
# res =res*a[0]
# print(res)

# a = list(map(int,input().split()))
# sum = a[0]
# for i in range(1,a[3]):
#     sum=sum*a[1]+a[2]
#
# print(sum)

# a,b,c = map(int,input().split())
# i=max(a,b,c)
# while(True):
#     if i%a==0 and i%b==0 and i%c==0:
#         print(i)
#         break
#     else:
#         i=i+1
# a= int(input())
# b = list(map(int,input().split()))
#
# c = [0 for i in range(23)]
#
# for i in range(len(b)):
#     c[b[i-1]-1]=c[b[i-1]-1]+1
#
#
# for i in range(len(c)):
#     print(c[i])

# b = input()
# a = list(map(int,input().split()))
#
# for i in range(len(a)):
#     print(a[-(i+1)], end=" ")
#
#

# b = input()
# a = list(map(int,input().split()))
#
# print(min(a))


# n = int(input())
# l=[0 for i in range(n)]
# for i in range(n):
#    l[i]=input()
#
# a = [[0]*19 for _ in range(19)]
# # print(a)
#
#
# for i in range(len(l)):
#     z,x = l[i].split()
#     a[int(z)-1][int(x)-1]=1
#
# for i in range(19):
#     for j in range(19):
#         if j ==18:
#             print(a[i][j])
#         else:
#             print(a[i][j],end=" ")

# a = [[0]*19 for _ in range(19)]
#
# for i in range(19):
#     k = list(map(int,input().split()))
#     for j in range(len(k)):
#         a[i][j]=k[j]
#
#
# n = int(input())
#
#
# l=[0 for i in range(n)]
# for i in range(n):
#    l[i]=input()
#
# for i in range(len(l)):
#     z,x = l[i].split()
#     for j in range(19):
#         for p in range(19):
#             if j== int(z)-1 or p == int(x)-1:
#
#                 if  a[j][p]==1:
#                     a[j][p]=0
#                 else:
#                     a[j][p]=1
#
# for i in range(len(l)):
#     z,x = l[i].split()
#     for j in range(19):
#         for p in range(19):
#             if j== int(z)-1 and p == int(x)-1:
#
#                 if  a[j][p]==1:
#                     a[j][p]=0
#                 else:
#                     a[j][p]=1
#
#
# for i in range(19):
#     for j in range(19):
#         if j ==18:
#             print(a[i][j])
#         else:
#             print(a[i][j],end=" ")
#
# m,n = map(int, input().split())
# pan = [[0]*n for _ in range(m)]
# ea = int(input())
#
# target = [_ for _ in range(ea)]
#
# for i in range(ea):
#     target[i]= input()
#
# for i in range(len(target)):
#     a, b, c, d = map(int, target[i].split())
#     if d == 0:
#         for j in range(a):
#             pan[c - 1][d - 1 + j] = 1
#     elif d == 1:
#         for j in range(a):
#             pan[c - 1 + j][d - 1] = 1
#
# for i in range(m):
#     for j in range(n):
#         if j ==n-1:
#             print(pan[i][j])
#         else:
#             print(pan[i][j], end=" ")

target = [[_]*10 for _ in range(10)]

for i in range(10):
    a = list(map(int, input().split()))
    for j in range(len(a)):
        target[i][j]=a[j]
a=1
b=1
while(True):

    if target[a][b]==2:
        target[a][b]=9
        break
    elif target[a][b]==0:
        target[a][b]=9
        if target[a][b+1]==2:
            target[a][b+1]=9
            break
        elif target[a][b+1]==0:
            b=b+1
        elif target[a][b+1]==1:
            if target[a+1][b]==0:
                a=a+1
            elif target[a+1][b]==2:
                target[a + 1][b] = 9
                break
            else:
                break



for i in range(10):
    for j in range(10):
        print(target[i][j],end=" ")
    print(end="\n")