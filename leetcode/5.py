class Solution:
    def longestPalindrome(self, s: str) -> str:
        ss = '$#'
        for c in s:
            ss += c + '#'
        ss += '@'
        dp = [0 ] *len(ss)

        mid = 0
        mx = 0
        s = 0
        mx_len = 1

        for i in range(1, len(ss) - 1):
            if i < mx:
                dp[i] = min(dp[2 *mid - i], mx - i)
            else:
                dp[i] = 1

            while ss[i + dp[i]] == ss[i - dp[i]]:
                dp[i] += 1

            if mx < i + dp[i]:
                mx = i + dp[i]
                mid = i

            if mx_len < dp[i]:
                s = i
                mx_len = dp[i]

        return ss[s - mx_len + 1: s + mx_len].replace('#', '').replace('$', '').replace('@', '')