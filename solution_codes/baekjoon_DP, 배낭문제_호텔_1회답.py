c, n = map(int, input().split())
inv = [list(map(int, input().split())) for _ in range(n)]

'''
배낭 문제
inv : cost, ppl
k명 확보했을때 최소 비용
f(k+ppl) = min(f(k+ppl), f(k) + cost))
'''

dp_tab = [float('inf')]*(c+101) # 0~c+100명
for cost, ppl in inv:
    dp_tab[ppl] = min(dp_tab[ppl], cost) 

for k in range(c+1):
    for cost, ppl in inv:
        dp_tab[k+ppl] = min(dp_tab[k+ppl], dp_tab[k] + cost)

print(min(dp_tab[c:]))

