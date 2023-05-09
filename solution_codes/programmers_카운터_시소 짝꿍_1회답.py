from collections import Counter
import math

def solution(weights):
    answer = 0
    c = Counter(weights)
    # 먼저 무게 같은 사람을 빼기
    for w in c.keys():
        if c[w] >= 2: 
            # 2명이상이면 nC2 로 쌍의 수를 더하기
            answer += math.comb(c[w],2)
    # print('same:', answer)
    weights = set(weights) # 같은 무게끼리는 처리했으니 중복을 지움
    # 2:3, 2:4, 3:4 
    for w in weights: # 다른 무게들별로
        if w*3/2 in weights:
            answer += (c[w] * c[w*3/2])
        if w*2 in weights:
            answer += (c[w] * c[w*2])
        if w*4/3 in weights:
            answer += (c[w] * c[w*4/3])
    return answer