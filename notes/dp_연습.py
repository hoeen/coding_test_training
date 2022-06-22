def fibo(x, memo={}): # x번째 수 피보나치 - 탑다운, 메모이제이션
    if x in memo:
        return memo[x]
    else:
        if x <= 0:
            return False
        elif x == 1 or x == 2:
            ans = 1
            memo[x] = ans
            return ans
        else:
        # f(k+1) = f(k) + f(k-1)
            ans = fibo(x-2,memo) + fibo(x-1,memo)
            memo[x] = ans
            return ans

def fibo_tab(x): # x번째 수 반환
    tab = [0]*x
    tab[0] = 1
    tab[1] = 1
    for i in range(x-2): # 0~x-1
        tab[i+2] = tab[i] + tab[i+1]
    return tab[x-1]

import time
t0 = time.time()
print(fibo(1500))
print(time.time() - t0)
t0 = time.time()
print(fibo_tab(1500))
print(time.time() - t0)

        



# 1 1 2 3 5 8 13 21 34 55 89 144