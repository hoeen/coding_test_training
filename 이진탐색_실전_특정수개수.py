from bisect import bisect_left, bisect_right

'''
bisect_left(list, a) : 정렬된 list내에서, a를 왼쪽에 삽입할 인덱스를 구함
bisect_right(list, a): 정렬된 list내에서, a를 오른쪽 삽입할 인덱스를 구함
'''

def binary_search(array, value, start, end):
    if start > end:
        return None
    else:
        mid = (start + end) // 2
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            return binary_search(array, value, start, mid-1)
        else:
            return binary_search(array, value, mid+1, end)

n, x = map(int, input().split())

array = list(map(int, input().split()))

left_idx = bisect_left(array, x)
right_idx = bisect_right(array, x)

if left_idx != right_idx:
    print(right_idx - left_idx)
else:
    print(-1)


