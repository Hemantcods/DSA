class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        MOD = 10**9 + 7

        dp = [[[-1]*2 for _ in range(zero+1)] for _ in range(one+1)]

        def solve(onesleft, zerosleft, last_time_one):
            if onesleft == 0 and zerosleft == 0:
                return 1

            if dp[onesleft][zerosleft][last_time_one] != -1:
                return dp[onesleft][zerosleft][last_time_one]

            res = 0

            if last_time_one:
                for i in range(1, min(zerosleft, limit) + 1):
                    res += solve(onesleft, zerosleft - i, 0)
            else:
                for i in range(1, min(onesleft, limit) + 1):
                    res += solve(onesleft - i, zerosleft, 1)

            dp[onesleft][zerosleft][last_time_one] = res % MOD
            return dp[onesleft][zerosleft][last_time_one]

        start_with_one = solve(one, zero, 1) if one > 0 else 0
        start_with_zero = solve(one, zero, 0) if zero > 0 else 0

        return (start_with_one + start_with_zero) % MOD