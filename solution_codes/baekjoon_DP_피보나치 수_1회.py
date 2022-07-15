import time
from contextlib import contextmanager

class Timer:
    def __init__(self, f):
        self.func = f
    def __call__(self, *args, **kwargs):
        t0 = time.time()
        res = self.func(*args, **kwargs)
        print(f'[{self.func.__name__}] executed in {time.time() - t0}s')
        return res

@contextmanager
def time_elapsed():
    t0 = time.time()
    yield
    print(f'task executed in {time.time() - t0}s')


n = int(input())


f1 = 0

# def fib_recur(n):
#     global f1
#     if n == 1 or n == 2:
#         f1 += 1
#         return 1
#     else: 
#         return fib_recur(n-1) + fib_recur(n-2)

# fib_recur(n)
# print(f1)

@Timer
def fib_dp(n):
    f2 = 0
    tab = [0]*(n+1)  # 0 ~ n
    tab[1], tab[2] = 1, 1
    for i in range(3,n+1):
        f2 += 1
        tab[i] = tab[i-1] + tab[i-2]
    print('f2 called:', f2)
    return tab[-1]

print(fib_dp(n))


f3 = 0
memo = {}
memo[1] = 1
memo[2] = 1

def fib_dp_recur(n, memo=memo):
    global f3
    f3 += 1
    if n in memo:
        return memo[n]
    else:
        if n-1 in memo and n-2 in memo:
            memo[n] = memo[n-1] + memo[n-2]
        return fib_dp_recur(n-1) + fib_dp_recur(n-2)

with time_elapsed():
    print(fib_dp_recur(n))

print('f3 called:', f3)
