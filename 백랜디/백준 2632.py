import sys, bisect
input = sys.stdin.readline

dest = int(input())

N, M = map(int, input().split())

pizza_A = [0]
pizza_B = [0]

for i in range(N) :
    pizza_A.append(pizza_A[-1] + int(input()))

for j in range(M) :
    pizza_B.append(pizza_B[-1] + int(input()))

# print(pizza_A)
# print(pizza_B)

pieces_A = []
pieces_B = []

ans = 0
        
def push_piece(pi, pieces) :
    global ans
    if pi == dest :
        ans += 1
    elif pi < dest :
        pieces.append(pi)

for i in range(N) :
    for j in range(i + 1, N + 1) :
        push_piece(pizza_A[j] - pizza_A[i], pieces_A)
        if i > 0 and j < N :
            push_piece(pizza_A[-1] - (pizza_A[j] - pizza_A[i]), pieces_A)

for i in range(M) :
    for j in range(i + 1, M + 1) :
        push_piece(pizza_B[j] - pizza_B[i], pieces_B)
        if i > 0 and j < M :
            push_piece(pizza_B[-1] - (pizza_B[j] - pizza_B[i]), pieces_B)

pieces_A.sort()
pieces_B.sort()


# print(pieces_A)
# print(pieces_B)

b_lst = []
b_cnt = []

for i in range(len(pieces_B)) :
    if not b_lst or b_lst[-1] < pieces_B[i] :
        b_lst.append(pieces_B[i])
        b_cnt.append(1)
    else :
        b_cnt[-1] += 1

# print(b_lst)
# print(b_cnt)

def bi_search(a) :
    global ans
    start = 0
    end = len(b_lst) - 1
    while start <= end :
        mid = (start + end) // 2
        if a + b_lst[mid] == dest :
            ans += b_cnt[mid]
            return
        elif a + b_lst[mid] < dest :
            start = mid + 1
        else :
            end = mid - 1

for p in pieces_A :
    if p < dest :
        bi_search(p)
    elif p == dest :
        ans += 1

print(ans)