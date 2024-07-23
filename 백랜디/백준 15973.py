import sys
input = sys.stdin.readline

def is_face(box1, box2) :
    #x랑 y가 다 겹쳐있어야 함.    
    if (box2[0][0] < box1[0][1] <= box2[0][1] or box1[0][0] < box2[0][1] <= box1[0][1]) and (box2[1][0] < box1[1][1] <= box2[1][1] or box1[1][0] < box2[1][1] <= box1[1][1]) :
        return True
    return False

def is_line(box1, box2) :
    #x나 y중 하나만 겹치고, 나머지 하나는 같은 값
    
    #x가 겹치고 y가 같은값임
    if (box2[0][0] < box1[0][1] <= box2[0][1] or box1[0][0] < box2[0][1] <= box1[0][1]) and (box1[1][1] == box2[1][0] or box1[1][0] == box2[1][1]) :
        return True
    
    #y가 겹치고 x가 같은값임
    if (box2[1][0] < box1[1][1] <= box2[1][1] or box1[1][0] < box2[1][1] <= box1[1][1]) and (box1[0][1] == box2[0][0] or box1[0][0] == box2[0][1]) :
        return True
    return False

def is_point(box1, box2) :
    #딱 한점이 아예 같은 값
    
    if (box1[0][1] == box2[0][0] or box2[0][1] == box1[0][0]) and (box1[1][1] == box2[1][0] or box2[1][1] == box1[1][0]) :
        return True
    return False

x1, y1, x2, y2 = map(int, input().split())
box1 = [(x1, x2), (y1, y2)]
    
x1, y1, x2, y2 = map(int, input().split())
box2 = [(x1, x2), (y1, y2)]

# print(box1, box2)

if is_face(box1, box2) :
    print("FACE")
elif is_line(box1, box2) :
    print("LINE")
elif is_point(box1, box2) :
    print("POINT")
else :
    print("NULL")