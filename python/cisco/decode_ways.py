
def numDecodings(s: str) -> int:
    n = len(s)
    if not s:
        return 0
    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 0 if s[0] == '0' else 1

    for i in range(2, len(dp)):
        if s[i - 1] != '0':
            dp[i] += dp[i - 1]
        td = int(s[ i -2:i])
        if td >= 10 and td <= 26:
            dp[i] += dp[ i -2]
    return dp[len(s)]
