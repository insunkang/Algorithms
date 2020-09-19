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

a,b,c=map(int,input().split("."))

# print(a,b,c)
print("%04d" % a, end=".")
print("%02d" % b, end=".")
print("%02d" % c)