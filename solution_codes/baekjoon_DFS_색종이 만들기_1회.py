n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]

# board = [ 
# [1, 1, 0, 0, 0, 0, 1, 1],
# [1, 1, 0, 0, 0, 0, 1, 1],
# [0, 0, 0, 0, 1, 1, 0, 0],
# [0, 0, 0, 0, 1, 1, 0, 0],
# [1, 0, 0, 0, 1, 1, 1, 1],
# [0, 1, 0, 0, 1, 1, 1, 1],
# [0, 0, 1, 1, 1, 1, 1, 1],
# [0, 0, 1, 1, 1, 1, 1, 1],
# ]

white = 0
blue = 0

def sum_pap(pa):
    res = 0
    for x in range(len(pa)):
        res += sum(pa[x])
    # print(res)
    if res == 0: return 0
    elif res == len(pa)**2: return 1
    else: return -1

def func(pa):
    global white, blue
    # print('print pa')
    # for p in pa:
    #     print(p)
    if sum_pap(pa) == 0:
        white += 1
        return
    elif sum_pap(pa) == 1:
        blue += 1
        return
    else:
        N = len(pa)
        if N == 1: return
        # print(N, sum_pap(pa))
        # print([p[0:(N//2)] for p in pa[:N//2]])
        func([p[0:(N//2)] for p in pa[:N//2]])
        func([p[(N//2):] for p in pa[:N//2]])
        func([p[0:(N//2)] for p in pa[N//2:]])
        func([p[(N//2):] for p in pa[N//2:]])

func(board)
print(white)
print(blue)
    
    

    