from itertools import combinations
# import time

ans_list = [0]
len = 1
while len < 11:
    
    for i in range(1, 10):
        if len > i+1: continue  
        
        for aft_num in combinations(list(range(i-1, -1, -1)),len-1): # 자릿수 - 1 만큼 경우의수
            num = str(i)
            for an in aft_num:
                num += str(an)
            ans_list.append(int(num))
    # time.sleep(2)
    # print(ans_list)
    len += 1  

ans_list.sort()

try:
    print(ans_list[int(input())])
except:
    print(-1)
