# # 10 15
# # 1 3 4 5 8 9 15 30 31 32
# # 0 0

# from itertools import count
# from operator import indexOf


# while True:
#     check = 1
#     trees = []
#     a,b = map(int,input().split(" "))
#     if a == 0 and b == 0:
#         break
#     tree_set = list(map(int,input().split(" ")))
#     # print(tree_set)
#     tree = []
#     now = 0
#     count_check = 1
#     for i in range(1,a):
#         # print(tree)
#         # print(count_check,check)
#         # print(now)
#         if now == 0:
#             tree.append(tree_set[i])
#             now = tree_set[i]
#         else:
#             if (now + 1) == tree_set[i]:
#                 tree.append(tree_set[i])
#                 now = tree_set[i]
#                 if i == (a-1):
#                         # print(trees)
#                         # tree.append(tree_set[i])
#                         trees.append(tree)
#             else:
#                 count_check+=1
                
#                 if count_check > check:
#                     # print("yes")
#                     trees.append(tree)
#                     check = len(tree)
#                     count_check = 1
#                     tree = [tree_set[i]]
#                     now = 0    
#                 else:
#                     if i == (a-1):
#                         # print(trees)
#                         tree.append(tree_set[i])
#                         trees.append(tree)
#                     else:
#                         tree.append(tree_set[i])
#                         now = tree_set[i]
#     answer = 0
#     for tree in trees:
#         if b in tree:
#             answer = len(tree) - 1
#             index = tree.index(b)
#             down_index = index
#             down_number = b
#             up_index = index
#             up_number = b
#             while True:
#                 down_index -= 1
#                 if down_index <0:
#                     break
#                 if tree[down_index] == (down_number-1):
#                     answer -= 1
#                 down_number -= 1
#             while True:
#                 up_index += 1
#                 if up_index > len(tree)-1:
#                     break
#                 if tree[up_index] == (up_number + 1):
#                     answer -= 1
#                 up_number += 1

#     print(answer)
#     # print(trees)               


    
from sys import stdin
from collections import defaultdict

while True:

    # 변수 초기화
    n, k = map(int, stdin.readline().split())
    if n==0 : break
    seq = list(map(int, stdin.readline().split()))
    tree = defaultdict(list)
    rootidx = -1
    for i in range(1, len(seq)):
        if seq[i]-seq[i-1]>1 :
            rootidx+=1
        tree[seq[rootidx]].append(seq[i])
        tree[seq[i]].append(seq[rootidx])

    # k의 부모, 조상 노드 찾기
    if rootidx==-1 :
        print(0)
        continue
    k_par = tree[k][0]
    if k_par > k :
        print(0)
        continue
    k_anc = tree[k_par][0]
    if k_anc > k_par :
        print(0)
        continue

    # k 부모를 제외한 손자들 계산
    sib = 0
    for par in tree[k_anc]:
        if par<k_anc or par==k_par : continue
        sib+=len(tree[par][1:])

    print(sib)

