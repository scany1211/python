# 给定一个整数数组nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例1：
# 输入：nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# 输出：6
# 解释：连续子数组[4, -1, 2, 1]
# 的和最大，为6 。
# 解法1：
# 动态规划
# 设 dp[i] 表示 [0..i] 中，以 nums[i] 结尾的最大子数组和，状态转移方程 dp[i] = nums[i] + max(dp[i - 1], 0)。
# 由于 dp[i] 只与子问题 dp[i-1] 有关，故可以用一个变量 f 来表示。

class Solution:
    def maxSubtree(self, nums):
        res = m = nums[0]
        for i in range(1, len(nums)):
            m = nums[i] + max(m, 0)
            res = max(res, m)
        return res
if __name__ == "__main__":
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    s=Solution()
    print(s.maxSubtree(nums))
