import sys
sys.setrecursionlimit = 5000
n, k = map(int, input().split())

# top-down
def find(x, t, memo: dict):
    # memoization - 확인해서 값 있으면 갱신하고 리턴
    if x == k:
        return t
    # k가 아닐 경우 메모하고 나옴
    if x-1 >= 0:
        if x-1 in memo:
            memo[x] = min(memo[x], memo[x-1]+1)
            return
        else:
            find(x-1, t+1, memo)
    if x+1 <= 100000:
        if x+1 in memo:
            memo[x] = min(memo[x], memo[x+1]+1)
            return
        else:
            find(x+1, t+1, memo)
    if 2*x <= 100000:
        if 2*x in memo:
            memo[x] = min(memo[x], memo[2*x])
        else:
            find(2*x, t, memo)

print(find(n, 0, dict()))



