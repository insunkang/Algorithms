n = int(input())
tree = list(map(int,input().split(" ")))

while True:
    if len(tree) > 2:
        print(tree[len(tree)//2])
        treeset = [tree[:len(tree)//2],tree[len(tree)//2+1:]]
        tree = treeset
    elif len(tree) == 1:
        print(tree[0])
        break
    else:
        if len(tree[0]) == 2:
            result = []
            for i in range(len(tree)):
                for j in range(2):
                    result.append(tree[i][j])
            print(*result)
            break
        else:
            result = []

            treeset = []
            # print(tree)
            for i in tree:
                subset = []
                result.append(i[len(i)//2])
                subset += i[:len(tree)//2]
                subset += i[len(tree) // 2 + 1:]
                treeset.append(subset)
            print(*result)
            tree = treeset


