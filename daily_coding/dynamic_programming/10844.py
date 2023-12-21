def main(N):
    dp = [[0 for _ in range(10)] for _ in range(N+1)]
    dp[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    
    for i in range(2, N+1):
        for j in range(0, 10):
            if j == 0:
                dp[i][j] = dp[i-1][j+1]
            elif j > 0 and j < 9:
                dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
            else:
                dp[i][j] = dp[i-1][j-1]
    print(sum(dp[N]) % 1000000000)

if __name__ == "__main__":
    N = int(input())
    main(N)
