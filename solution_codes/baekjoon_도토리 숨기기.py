n, k, d = map(int, input().split())

rules = [list(map(int, input().split())) for _ in range(k)]


# 이분 탐색 -> 
def check_last(box):
    count = 0
    max_st = 0
    for start, end, width in rules:
        if start <= box:
            st = start
            if max_st < st:
                max_st = st
            while st <= box and st <= end:
                count += 1
                st += width
                if max_st < st:
                    max_st = st
    return max_st, count

def binary_search(start, end):

    if start > end:
        return False
    else:
        mid = (start + end) // 2
        st, check = check_last(mid)
        if check == d:
            (st, check) == (mid, d):
            
            
        elif check < d: # 마지막보다 앞 - 뒤 탐색 
            return binary_search(mid+1, end)
        elif check > d: # 마지막 상자보다 뒤 - 앞 탐색
            return binary_search(start, mid)

print(binary_search(1, n))



