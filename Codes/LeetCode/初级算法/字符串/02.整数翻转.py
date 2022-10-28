class Solution:
    def reverse(self, x: int) -> int:
        if x == 0 or abs(x) > 214748364:
            return 0
        code = int(x / abs(x))
        x = abs(x)

        temp = x % 10
        x = x // 10
        while x > 0:
            temp *= 10

            temp += x % 10
            x = x // 10
        res = code * temp
        return res if abs(res) < 214748364 else 0


print(Solution().reverse(1534236469))
