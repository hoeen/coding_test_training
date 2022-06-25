# 내림차순으로 배치되며 최대한 적게 열외시키자.

n = int(input())
solds = list(map(int, input().split()))

# f(k) = max(f(k), f(i)+1) for i in range(1~k) if f(i) < f(k)

tab = [1]*n
solds.reverse()

for k in range(n): #0~n-1
    for i in range(k): #0~k-1
        if solds[i] < solds[k]:
            tab[k] = max(tab[k], tab[i]+1)

print(tab)
print(n - max(tab))

