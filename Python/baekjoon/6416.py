from collections import defaultdict


def is_tree(idx, ies, ns):
    if not ns:
        print(f'Case {idx} is a tree.')
        return

    check = ns - set(ies.keys())
    if len(check) != 1:
        print(f'Case {idx} is not a tree.')
        return

    for e in ies:
        if len(ies[e]) != 1:
            print(f'Case {idx} is not a tree.')
            return

    print(f'Case {idx} is a tree.')


inbound_edges = defaultdict(list)
nodes = set()
idx = 1
flag = False

while True:

    if flag:
        break

    line = input()

    if not line:
        continue
    else:
        for s in line.split('  '):
            a, b = map(int, s.split())

            if a == b == -1:
                flag = True
                break
            elif a == b == 0:
                is_tree(idx, inbound_edges, nodes)

                inbound_edges = defaultdict(list)
                nodes = set()
                idx += 1
            else:
                nodes.add(a)
                nodes.add(b)
                inbound_edges[b].append(a)