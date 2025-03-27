class Solution:
    # Optimized solution
    def arrangeCoins(self, n: int) -> int:
        left, right = 0, n
        while left <= right:
            k = (right + left) // 2
            curr = k * (k + 1) // 2
            if curr == n:
                return k
            if n < curr:
                right = k - 1
            else:
                left = k + 1
        return right

    # My solution
    def arrange_coins(self, n):
        count = 0
        i = 1
        while i <= n:
            count += 1
            n = n - i
            i += 1
        return count
