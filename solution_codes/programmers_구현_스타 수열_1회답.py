
from collections import Counter

def solution(a):
    max_len = 0
    c = Counter(a)
    for key in c.keys():
        value = c[key]
        if value > max_len:
            # 뒤의 두개 탐색하며 진행
            count = 0
            idx = 0
            while idx < len(a)-1:
                # 현재칸, 뒷칸 모두 아닌 경우 및 현재칸, 뒷칸이 같은 경우는 카운트 불가
                if (a[idx] != key and a[idx+1] != key) or (a[idx] == a[idx+1]):
                    idx += 1
                else:
                    count += 1
                    idx += 2
                    
            max_len = max(max_len, count)

    return max_len*2