n = int(input())


times, costs = [], []
for _ in range(n):
    t, p = map(int, input().split())
    times.append(t)
    costs.append(p)


# n일에 받는 최대수익 : f(t) = max(pi + f(t+ti), f(t+1))
tab = [0]*n
# 끝날 tab 기입
if times[-1] == 1:
    tab[-1] = costs[-1]

for i in range(n-2, -1, -1): #n-2 ~ 0
    next = i+times[i]
    if next > n:
        tab[i] = tab[i+1]
    elif next == n: 
        tab[i] = max(costs[i], tab[i+1])
    else:
        tab[i] = max(costs[i] + tab[next], tab[i+1])
        
    # print(tab)
# print(tab)
print(tab[0])
