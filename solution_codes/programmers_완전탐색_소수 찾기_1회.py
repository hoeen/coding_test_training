# ~ 11:00
from itertools import permutations
import numpy as np 

def solution(numbers):
    # 소수 판별? 2~sqrt(자기자신)까지 해서 나머지 계속 생기면 됨 
    def is_sosu(number):
        for i in range(2, int(np.sqrt(number))+1):
            if number%i == 0:
                return False
        return True
    
    answer = []
    
    perm = []
    for l in range(1, len(numbers)+1):
        perm += list(set(permutations(numbers, l)))
    
    
    # print(perm)
    for i in perm:
        num = int(''.join(i))
        if num in [0, 1]: continue
        # print(is_sosu(num))
        if is_sosu(num):
            answer.append(num)
            
    return len(set(answer))