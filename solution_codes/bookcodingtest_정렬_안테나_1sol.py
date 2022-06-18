n = int(input())


loc = list(map(int, input().split()))

loc.sort()
print(loc[ (len(loc)-1) // 2])
