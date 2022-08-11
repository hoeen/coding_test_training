from collections import deque

    
def ex1(queue1, queue2):
    q1, q2 = deque([q for q in queue1]), deque([q for q in queue2])
    temp = q1.popleft()
    q2.append(temp)
    return q1, q2

def ex2(queue1, queue2):
    q1, q2 = deque([q for q in queue1]), deque([q for q in queue2])
    temp = q2.popleft()
    q1.append(temp)
    return q1, q2

def solution(queue1, queue2):
    q = deque([])
    
    qsum = (sum(queue1) + sum(queue2))
    if qsum % 2 != 0 :
        return -1
    else:
        qsum = qsum // 2
        
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    
    
    # ex1, ex2를 반복하며 합이 같아질때까지 한다.
    # 불가능하거나 중복되는 경우는 어떻게 고려?
    # 지나왔던 값이 또 나오면 불가로 판단. 리턴시킴
    def dfs(queue1, queue2, count, memo=[]):
        # print(queue1, queue2, count, memo)
        if sum(queue1) == sum(queue2):
            return count
        else:
            if queue1 in memo or queue2 in memo:
                return -1
            else:
                
                if queue1:
                    memo.append(queue1)
                    new_queue1, new_queue2 = ex1(queue1, queue2)
                    dfs(new_queue1, new_queue2, count+1, memo)
                    memo.pop()
                if queue2:
                    memo.append(queue2)
                    new2_queue1, new2_queue2 = ex2(queue1, queue2)
                    dfs(new2_queue1, new2_queue2, count+1, memo)
                    memo.pop()
            
        
    answer = dfs(queue1, queue2, 0, [])
    
        
    
    # q.popleft()
    # q.append()
    return answer


