import sys

input = sys.stdin.readline

N = int(input())
answer = 0
trees = [[] for _ in range(N)]
root = -1
parents = list(map(int, input().split(" ")))
del_number = int(input())
for i in range(N):
    if parents[i] == -1:
        root = i
    else:
        trees[parents[i]].append(i)


# print(parents)
# print(trees)

def delete(trees, number):
    next_delete = []
    for i in trees[number]:
        next_delete.append(i)
    while len(trees[number]) != 0:
        del trees[number][0]
    trees[number].append(-1)
    for i in next_delete:
        delete(trees, i)


for i in range(len(trees)):
    if i == del_number:
        delete(trees, i)
    if del_number in trees[i]:
        trees[i].remove(del_number)

# print(trees)

for i in trees:
    if len(i) == 0:
        answer += 1
print(answer)
