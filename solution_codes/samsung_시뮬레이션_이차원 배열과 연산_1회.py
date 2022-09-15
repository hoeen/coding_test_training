# ~ 11:20 #40분   ~11:55  # 1시간 15분 만에 품.
r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

# 행이 더 크거나 같으면 R, 열이 더 크면 C
def measure():
    if len(A) >= len(A[0]):
        return 'R'
    else:
        return 'C'

def Asort(rc):
    global A
    r = len(A)
    c = len(A[0])
    # dict로 먼저 넣고, 그뒤에 튜플로 붙이고 정렬하기.
    if rc == 'C':
        # 역 행 전치
        Ac = [[A[i][j] for i in range(r)] for j in range(c)]
        A = [a[:] for a in Ac]
    
    total_list = []
    max_length = 0
    for al in A:
        dic = {}
        alist = []
        for a in al:
            if a == 0:
                continue
            if a not in dic:
                dic[a] = 1
            else:
                dic[a] += 1
        for key in dic:
            alist.append((key, dic[key]))
        alist.sort(key=lambda x: (x[1], x[0]))
        tu_list = []
        for a, b in alist:
            tu_list.append(a)
            tu_list.append(b)
        
        if max_length < len(tu_list):
            max_length = len(tu_list)
        total_list.append(tu_list)
    
    # 최대길이보다 짧은 리스트는 0을 추가
    tt_list = [t[:] for t in total_list]
    for u in range(len(total_list)):
        dif = max_length - len(total_list[u])
        if dif > 0:
            tt_list[u] = total_list[u] + [0]*dif
    
    A = [t[:] for t in tt_list] 
    # 역 행 다시 전치
    if rc == 'C':
        Ac = [[A[i][j] for i in range(len(A))] for j in range(len(A[0]))]
        A = [a[:] for a in Ac]

    return 

ti = 0
while ti <= 100:

    res = 'not found'
    if r-1 >= len(A) or c-1 >= len(A[0]):
        pass
    else:
        if A[r-1][c-1] == k:
            res = 'found'
            print(ti)
            break

    if ti == 100 and res != 'found':
        print(-1)
        break
    ti += 1           
    m = measure()
    Asort(m)

    if len(A) > 100 or len(A[0]) > 100:
        A = [a[:min(100, len(A[0]))] for a in A[:min(100, len(A))]]
    