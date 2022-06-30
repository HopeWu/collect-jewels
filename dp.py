class JewelStone:
    def __init__(self, weight=0, value=0):
        self.weight = weight
        self.value = value


class Solution:
    def getMaxValue(self, stones: [JewelStone], capacity: int) -> int:
        n = len(stones)
        dp = [0]*(capacity+1)
        for i in range(n):
            w = stones[i].weight
            v = stones[i].value
            for j in range(capacity, 0, -1):
                if j >= w:
                    dp[j] = max(dp[j-w] + v, dp[j])
                else:
                    dp[j] = dp[j]

        return dp[capacity]


li = [(1, 3), (2, 4), (3, 5), (4, 7)]
stones = []

for i in li:
    stones.append(JewelStone(weight=i[0], value=i[1]))


solution = Solution()
print(solution.getMaxValue(stones, 5))
