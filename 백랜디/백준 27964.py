import sys
input = sys.stdin.readline

N = int(input())
cheeses = list(input().split())

def can_make_Quattro() :
    toppings = []
    for ch in cheeses :
        now = ch[-6:]
        if now == "Cheese" :
            if ch not in toppings :
                toppings.append(ch)
                if len(toppings) >= 4 :
                    print("yummy")
                    return
    print("sad")
    return

can_make_Quattro()
