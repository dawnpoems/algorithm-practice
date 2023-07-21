import sys
from collections import deque
input = sys.stdin.readline
import ast

t = int(input())

for i in range(t) :
    func = list(input().strip())
    n = int(input())
    array = ast.literal_eval(input().strip())

    queue = deque(array)
    error_flag = False
    r_flag = False

    for f in func :
        if f == "R" :
            if r_flag :
                r_flag = False
            else :
                r_flag = True
        else :
            if len(queue) <= 0 :
                error_flag = True
                break
            elif r_flag :
                queue.pop()
            else :
                queue.popleft()
    
    # print("---------" + str(i))
    if error_flag :
        print("error")

    else :
        if r_flag :
            queue.reverse()
        nums = ",".join(map(str, queue))
        output = "[" + nums + "]"
        print(output)