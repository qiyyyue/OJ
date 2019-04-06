class Solution:
    def nthMagicalNumber(self, N: int, A: int, B: int) -> int:
        def gcd(a: int, b: int) -> int:
            return a if b == 0 else gcd(b, a % b)

        l, r = 0, 2000000000000000000
        if A < B:
            A, B = B, A
        lcm = A * B / gcd(A, B)

        tmp = 0
        while l < r:
            mid = (r + l) // 2
            tmp_count = mid // A + mid // B - mid // lcm
            if tmp_count < N:
                l = mid + 1
            else:
                r = mid
        return r % (10 ** 9 + 7)

s = Solution()
s.nthMagicalNumber(1, 2, 3)