# 최댓값, 최솟값을 한번에 O(logn)으로 빼는 방법?
# 1. 그때그때 정렬
def solution(operations):
    answer = []
    queue = []
    for op in operations:
        com, num = op.split()
        num = int(num)
        if com == 'I':
            queue.append(num)
        elif com == 'D' and len(queue) > 0:
            if num == 1:
                queue.sort()
                queue.pop() # 최댓값 삭제  
            elif num == -1:
                queue.sort()
                queue.pop(0) # 최솟값 삭제
        
    return [max(queue), min(queue)] if queue else [0, 0]