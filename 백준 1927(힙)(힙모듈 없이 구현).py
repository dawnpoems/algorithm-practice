import sys

heap = []
n = int(sys.stdin.readline())

for i in range(n):
    num = int(sys.stdin.readline())
    if num == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap.pop(0))
            if len(heap) >= 2:
                heap.insert(0, heap[-1])
                del heap[-1]
                del_index = 0
                child_del = 1
                while child_del < len(heap) - 1 and heap[del_index] > heap[child_del]:
                    heap[child_del], heap[del_index] = heap[del_index], heap[child_del]
                    del_index = child_del
                    child_del = del_index*2

    else:
        heap.append(num)
        end_index = len(heap) - 1
        while len(heap) >= 1 and heap[end_index//2] > heap[end_index]:
            heap[end_index//2], heap[end_index] = heap[end_index], heap[end_index//2]
            end_index = end_index//2
