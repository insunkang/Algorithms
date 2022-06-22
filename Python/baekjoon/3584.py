from collections import defaultdict, deque

cycle = int(input())
for _ in range(cycle):
    N = int(input())
    trees = defaultdict(list)
    reverse_trees = defaultdict(int)
    # nodes = [[i] for i in range(N+1)]
    for _ in range(N - 1):
        a, b = map(int, input().split(" "))
        reverse_trees[b] = a
        trees[a].append(b)
    # for i in range(1,N+1):
    # 	q = deque()
    # 	for j in trees[i]:
    # 		q.append(j)
    # 		nodes[i].append(j)
    # 	while q:
    # 		nowq = q.popleft()
    # 		now = trees[nowq]
    # 		for k in now:
    # 			q.append(k)
    # 			nodes[i].append(k)
    a, b = map(int, input().split(" "))
    parenta = []
    parentb = []
    q = deque()
    q.append(a)
    while q:
        now = q.popleft()
        if now == 0:
            break
        parenta.append(now)
        q.append(reverse_trees[now])

    qb = deque()
    qb.append(b)
    while qb:
        now = qb.popleft()
        if now == 0:
            break
        parentb.append(now)
        qb.append(reverse_trees[now])

    # print(parenta)
    # print(parentb)
    parenta.reverse()
    parentb.reverse()

    index = 0
    answer = parenta[index]
    while True:
        if len(parenta) == index or len(parentb) == index:
            print(answer)
            break
        if parenta[index] != parentb[index]:
            print(answer)
            break
        answer = parenta[index]
        index += 1

# print(reverse_trees)
