# ~3:00
from collections import deque

possible = False # 처음 홀수 판별
init1, init2 = None, None
def solution(queue1, queue2, trial=0, min_trial=None):
    global possible, init1, init2
    # 먼저, 모든 합이 홀수면 불가.
    if not possible:
        if sum(queue1+queue2)%2 == 1:
            return -1
        else:
            possible = True
            init1, init2 = [q for q in queue1], [q for q in queue2]
            print('init', init1, init2)
    if possible:
        nq1 = deque([i for i in queue1])
        nq2 = deque([i for i in queue2])
        if sum(nq1) == sum(nq2):
            print('same', nq1, nq2)
            if min_trial is None or min_trial > trial:
                min_trial = trial
            return min_trial
        elif sum(nq1) > sum(nq2):
            if len(nq2) == 1:
                return -1
            else:
                print('left > right')
                popped = nq1.popleft() # pop
                nq2.append(popped) # insert
                # 처음과 같아지면 종료
                if list(nq1) == init1 or list(nq1) == init2: # and list(nq2) == init2:
                    if min_trial:
                        return min_trial
                    else:
                        return -1
                # 아니면 trial +1 하고 넘어감
                else:
                    trial += 1
                print(nq1, nq2)
        else:
            if len(nq2) == 1:
                return -1
            else:
                print('left < right')
                popped = nq2.popleft()
                nq1.append(popped)
                # 처음과 같아지면 종료
                if list(nq1) == init1 or list(nq1) == init2: # and list(nq2) == init2:
                    if min_trial:
                        return min_trial
                    else:
                        return -1
                # 아니면 trial +1 하고 넘어감
                else:
                    trial += 1
                print(nq1, nq2)
    
        return solution(nq1, nq2, trial, min_trial)
    
    
# queue1 = [3,2,7,2]
# queue2 = [4,6,5,1]
# queue1 = [1,2,1,2]
# queue2 = [1,10,1,2]
queue1 = [1,100,1]
queue2 = [2,3,2,3]

import random

# queue1 = [1,10,13,5,8,28,9,12]
# queue2 = [6,7,3,1,2,50,4,17]

# queue1 = [2]
# queue2 = [1]

# queue1 = [27, 17, 90, 44, 37, 49, 50, 48, 70,  8, 66,  4, 33, 58, 53,  3, 63,
#        60, 18, 40, 93, 53, 12, 79, 36, 27, 23, 37, 35, 32,  5, 58, 75, 34,
#        35, 88, 26, 95, 86, 26, 52, 63, 80, 94, 12, 36, 87, 14, 96, 80, 34,
#        27, 92, 98, 79, 18, 39, 77, 95, 57, 81, 46, 90, 12, 56, 14, 88, 65,
#        23, 83, 45, 79, 17, 20, 90, 51, 38, 66, 93, 26, 17, 31, 39, 54, 67,
#        66, 67, 63,  9, 66, 21, 86, 87, 37, 34, 44, 58, 84, 73,  9]
# queue2 = [95, 23, 10, 54, 99, 91, 10, 53, 94, 81, 86, 58, 81, 17, 86, 88, 69,
#        66, 51, 38, 43, 24, 71, 78, 10, 97,  3, 91, 25, 85, 28, 77,  4, 12,
#        10,  5, 44, 30, 99, 86, 69, 94, 12, 91, 45, 75, 47, 75, 47, 33, 49,
#        86, 43, 48, 37, 16, 98, 77, 59, 59, 93, 88, 12, 86, 40, 42, 28, 67,
#        31,  6, 60, 77, 27, 53, 88, 10, 50, 44, 65, 41, 69,  5, 99, 53, 62,
#        62, 29, 20, 70, 86, 45, 53, 21, 98, 91, 86, 45, 28, 47, 3]
print(solution(queue1, queue2, 0, None))
