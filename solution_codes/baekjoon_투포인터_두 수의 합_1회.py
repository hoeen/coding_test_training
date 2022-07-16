n = int(input())
seq = list(map(int, input().split()))
x = int(input())

# n = 9 
# seq = [5,12,7,10,9,1,2,3,11]
# x = 13

# 2 pointers
left = 0 
right = n-1
seq.sort()

ans = 0
while left < right:
    if seq[left] + seq[right] == x:
        ans += 1
        right -= 1
    elif seq[left] + seq[right] > x:
        right -= 1
    else:
        left += 1
print(ans)
