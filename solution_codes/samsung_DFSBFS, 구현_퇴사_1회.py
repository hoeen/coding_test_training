# 2:00 ~ 3:30
'''
N일동안 최대한많은 상담.
하루에 하나씩 다른사람 상담. 소요기간 Ti, 받는금액 Pi
상담 했을때, 최대수익 구하라.
'''
# n = int(input())

# cons_list = []
# for _ in range(n):
#     cons_list.append(list(map(int, input().split())))

# # 예시 1
# n = 7
# cons_list = [ 
#     [3,10],
#     [5,20],
#     [1,10],
#     [1,20],
#     [2,15],
#     [4,40],
#     [2,200]
# ]

# # 예시 2
# n = 10
# cons_list = [ 
#     [1,1],
#     [1,2],
#     [1,3],
#     [1,4],
#     [1,5],
#     [1,6],
#     [1,7],
#     [1,8],
#     [1,9],
#     [1,10]
# ]

# # 예시 3
# n = 10
# cons_list = [ 
#     [5,10],
#     [5,9],
#     [5,8],
#     [5,7],
#     [5,6],
#     [5,10],
#     [5,9],
#     [5,8],
#     [5,7],
#     [5,6]
# ]

# # 예시 4
# n = 10
# cons_list = [ 
#     [5,50],
#     [4,40],
#     [3,30],
#     [2,20],
#     [1,10],
#     [1,10],
#     [2,20],
#     [3,30],
#     [4,40],
#     [5,50]
# ]

# 만든 예시 1
# n = 15
# cons_list = [ [3,50]]*15

# 만든 예시 2
# n = 3
# cons_list = [ 
#     [4,10],
#     [3,20],
#     [2,50]
# ]

# 만든 예시 3
# n = 11
# cons_list = [ 
#     [5,10],
#     [5,10],
#     [5,200],
#     [5,10],
#     [5,10],
#     [5,10],
#     [5,10],
#     [5,10],
#     [5,10],
#     [5,10],
#     [5,10],
    
# ]

# 만든 예시 4
n = 2
cons_list = [
    [3,1],
    [1,1]
]

money_cand = []
def max_price(k, earned):  # 처음에 k = 0, earned = 0, date =[]
    if k >= n:
        money_cand.append(earned)
        return
    else:
        tk, pk = cons_list[k][0], cons_list[k][1]
        # exit : 벗어나는경우
        # k+1 때 일한다면
        if k+1 < n:
            max_price(k+1, earned)
        
        if k+tk > n:
            money_cand.append(earned)
            return
        else:
            # k때 일한다면
            earned_k = earned + pk
            max_price(k+tk, earned_k)
            

max_price(0,0)
print(money_cand)
print(max(money_cand))