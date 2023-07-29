import sys
input = sys.stdin.readline

n = int(input())

s = []

for i in range(n) :
    c = input().strip()
    if c == "all" :
        s = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20"]
    elif c == "empty" :
        s = []
    else :
        com, x = c.split()
        if com == "add" :
            if x not in s :
                s.append(x)
        elif com == "remove" :
            if x in s :
                s.remove(x)
        elif com == "check" :
            # print("////")
            if x in s :
                print(1)
            else :
                print(0)
        else :
            if x in s :
                s.remove(x)
            else :
                s.append(x)
    # print(s)