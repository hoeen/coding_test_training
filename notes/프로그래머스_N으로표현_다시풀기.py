from collections import deque

def solution(N, number):
    tab = [0]*N*int(1e6)
    # N, NN, NNN 등 먼저 집어넣기
    multi = N
    count = 1
    while multi < len(tab):
        tab[multi] = count
        multi = 10*multi + N
        count += 1
    
    stack = deque([])
    stack.append(N)
    while stack:
        breakpoint()
        num = stack.pop()
        cand_cal = [num+5, num-5, num*5, num//5]
        new_cal = []
        for c in cand_cal:
            if 1 <= c < len(tab):
                new_cal.append(c)
        print(num)
        print(new_cal)
        for c in new_cal:
            if tab[c] > tab[num] + 1:
                tab[c] = tab[num] + 1
            elif tab[c] == 0:
                tab[c] = tab[num] + 1
                stack.append(c)
            else: 
                continue
    
    answer = tab[number]
    return answer

print(solution(5, 12))