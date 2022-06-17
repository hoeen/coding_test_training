# ~2:00
def binary_search(array, start, end):
    if start > end:
        return -1
    else:
        mid = (start + end) // 2
        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            # 더 작은쪽 조사
            return binary_search(array, start, mid-1)
        else:
            return binary_search(array, mid+1, end)
    

n = int(input())
array = list(map(int, input().split()))

print(binary_search(array, 0, n-1))

