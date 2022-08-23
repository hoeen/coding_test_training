def solution(N, number):
    dp = [set() for _ in range(9)]
    for i in range(1, 9): # 1~8
        dp[i].add(int(str(N)*i))
        # 더해서 i가 되는 dp 끼리 연산하기
        for j in range(1, i):
            for op1 in dp[j]:
                for op2 in dp[i-j]:
                    dp[i].add(op1 + op2)
                    dp[i].add(op1 - op2)
                    dp[i].add(op1 * op2)
                    if op2 != 0:
                        dp[i].add(op1 // op2)
                    if op1 != 0:
                        dp[i].add(op2 // op1)
        if number in dp[i]:
            return i
    return -1 