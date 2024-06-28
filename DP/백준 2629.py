import sys
input = sys.stdin.readline

N = int(input())

weights = list(map(int, input().split()))

M = int(input())

marbles = list(map(int, input().split()))

mx = 40000

def is_balance(m) :
    dp_left = [False] * (mx + 1)
    dp_left[m] = True
    
    for w in weights :
        for i in range(mx, -1, -1) :
            if i - w >= 0 :
                if dp_left[i - w] :
                    dp_left[i] = True
                if dp_left[i] and dp_right[i] :
                    return True
    return False
    
for m in marbles :
    dp_right = [False] * (mx + 1) #이 무게를 만들 수 있는가?
    dp_right[0] = True
    
    for w in weights :
        for i in range(mx, -1, -1) :
            if i - w >= 0 :
                if dp_right[i - w] :
                    dp_right[i] = True

    if is_balance(m) :
        print("Y", end=" ")
    else :
        print("N", end=" ")
        