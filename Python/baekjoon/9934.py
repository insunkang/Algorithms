n = int(input())
tree = list(map(int,input().split(" ")))

while True:
    # print(tree)
    if len(tree) == 2**n-1:
        print(tree[len(tree)//2])
        treeset = [tree[:len(tree)//2],tree[len(tree)//2+1:]]
        tree = treeset
    elif len(tree) == 1:
        print(tree[0])
        break
    else:
        if len(tree[0]) ==1:
            result = []
            for i in range(len(tree)):
                for j in range(1):
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
                a = i[:len(i)//2]
                # print(a,"a")
                # treeset.append(i[:len(tree)//2])
                b = i[len(i) // 2 + 1:]
                # print(b,"b")
                # treeset.append(i[len(tree) // 2 + 1:])
                treeset.append(a)
                treeset.append(b)
            print(*result)
            tree = treeset


