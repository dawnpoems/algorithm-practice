import sys

n = int(sys.stdin.readline().rstrip())
nodes = list(map(int, sys.stdin.readline().split()))

node_list = [[]]

node_list[0].append(str(nodes[(len(nodes) // 2)]))  # 루트를 리스트에 넣기


def visit(tree, x):  # x는 깊이값
    if len(node_list) <= x:
        node_list.append([])

    if len(tree) <= 1:
        return

    left = tree[:(len(tree) // 2)]  # 왼쪽 배열
    right = tree[(len(tree) // 2) + 1:]  # 오른쪽 배열

    node_list[x].append(str(left[(len(left) // 2)]))
    node_list[x].append(str(right[(len(right) // 2)]))

    visit(left, x+1)  # 왼쪽 배열로 실행
    visit(right, x+1)  # 오른쪽 배열로 실행


visit(nodes, 0)

for i in node_list:
    print(" ".join(i))
