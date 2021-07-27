# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
#
# result = 0
#
# def find(number, targetN):
#     global result
#     if len(number) == targetN:
#          result += 1
#          return
#     else:
#         if number[len(number)-1] == "1":
#             find(number + "0", targetN)
#         else:
#             find(number + "0", targetN)
#             find(number + "1", targetN)
#
# find("1", n)
#
# print(result)


s = [0, 1, 1]
for i in range(3, 91):
  s.append(s[i - 2] + s[i - 1])
n = int(input())
print(s[n])