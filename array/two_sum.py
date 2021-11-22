# 题目描述
# 给定一个整数数组nums和一个整数目标值target，请你在该数组中找出和为目标值的那两个整数，并返回它们的数组下标。
# 你可以假设每种输入只会对应一个答案。但是，数组中同一个元素在答案里不能重复出现。
# 你可以按任意顺序返回答案。
# 示例1：
# 输入：nums = [2, 7, 11, 15], target = 9
# 输出：[0, 1]
# 解释：因为
# nums[0] + nums[1] == 9 ，返回[0, 1] 。
# 示例2：
# 输入：nums = [3, 2, 4], target = 6
# 输出：[1, 2]
# 示例3：
# 输入：nums = [3, 3], target = 6
# 输出：[0, 1]
#
# 只会存在一个有效答案解法
# 用哈希表（字典）存放数组值以及对应的下标。
# 遍历数组，当发现
# target - nums[i]
# 在哈希表中，说明找到了目标值。

class Solution:
    def twoSum(self, nums, target):
        helper={}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in helper:
                return (helper[diff], i)
            helper[v] = i
            print(helper, type(helper))

if __name__ == "__main__":
    nums = [2, 1, 4, 7, 8, 9, 11]
    target = 9
    s = Solution()
    print(s.twoSum(nums, target))