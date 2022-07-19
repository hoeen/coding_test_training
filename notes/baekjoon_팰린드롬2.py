n = int(input())
seq = list(map(int, input().split()))
m = int(input())

dp_tab = [[False]*(n) for _ in range(n)]

for _ in range(m):
    s, e = map(int, input().split())
    s, e = s-1, e-1 
    
    ns, ne = s, e
    exited = False
    while ne - ns >= 1:
        if dp_tab[ns][ne]:
            dp_tab[s][e] = dp_tab[ns][ne]
            print(dp_tab[ns][ne])
            exited = True
            break
        else:
            if seq[ns] == seq[ne]:
                ns += 1
                ne -= 1
            else:
                exited = True
                dp_tab[s][e] = 0
                print(0)
                break
    if not exited:
        print(1)
        dp_tab[s][e] = 1

        



    
