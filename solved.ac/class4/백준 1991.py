import sys
input = sys.stdin.readline

n = int(input())

graph = []
order = []

for i in range(n) :
    root, left, right = input().strip().split()
    order.append(root)
    graph.append((left, right))

def front_search(start) :
    print(start, end="")
    idx = order.index(start)
    if graph[idx][0] != "." :
        front_search(graph[idx][0])
    if graph[idx][1] != "." :
        front_search(graph[idx][1])

def mid_search(start) :
    idx = order.index(start)
    if graph[idx][0] != "." :
        mid_search(graph[idx][0])
    print(start, end="")
    if graph[idx][1] != "." :
        mid_search(graph[idx][1])
    
def back_search(start) :
    idx = order.index(start)
    if graph[idx][0] != "." :
        back_search(graph[idx][0])
    if graph[idx][1] != "." :
        back_search(graph[idx][1])
    print(start, end="")

front_search("A")
print()
mid_search("A")
print()
back_search("A")