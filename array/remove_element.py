# 题目描述
# 给你一个数组nums和一个值val，你需要原地移除所有数值等于val的元素，并返回移除后数组的新长度。
# 不要使用额外的数组空间，你必须仅使用O(1)额外空间并原地修改输入数组。
# 元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

# 示例 1：
#
# 输入：nums = [3,2,2,3], val = 3
# 输出：2, nums = [2,2]
# 解释：函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。你不需要考虑数组中超出新长度后面的元素。例如，函数返回的新长度为 2 ，而 nums = [2,2,3,3] 或 nums = [2,2,0,0]，也会被视作正确答案。
#
# 示例 2：
#
# 输入：nums = [0,1,2,2,3,0,4,2], val = 2
# 输出：5, nums = [0,1,4,0,3]
# 解释：函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。注意这五个元素可为任意顺序。你不需要考虑数组中超出新长度后面的元素。

class Solution:
    def remove_el(self, nums, t):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == t:
                cnt += 1
            else:
                nums[i-cnt] = nums[i]
            print(cnt, i, nums)
        return len(nums)-cnt

# 题目描述
# 给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
# 示例:
# 输入: [0,1,0,3,12]
# 输出: [1,3,12,0,0]
# 说明:
#     必须在原数组上操作，不能拷贝额外的数组。
#     尽量减少操作次数。
    def remove_zero(self, nums):
        cnt = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt += 1
            else:
                nums[i-cnt] = nums[i]
        while cnt > 0:
            nums[-cnt] = 0
            cnt -= 1
        print(nums)

if __name__ == "__main__":
    nums = [0,1,2,2,3,0,4,2]
    target = 2
    s = Solution()
    # s.remove_el(nums, target)
    s.remove_zero(nums)