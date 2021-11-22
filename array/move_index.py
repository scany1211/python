# 给定一个数组，将数组中的元素向右移动k个位置，其中k是非负数。
# 进阶：
# 尽可能想出更多的解决方案，至少有三种不同的方法可以解决这个问题。你可以使用空间复杂度为O(1)的原地算法解决这个问题吗？
# 示例 1:
#
# 输入: nums = [1,2,3,4,5,6,7], k = 3
# 输出: [5,6,7,1,2,3,4]
# 解释:
# 向右旋转 1 步: [7,1,2,3,4,5,6]
# 向右旋转 2 步: [6,7,1,2,3,4,5]
# 向右旋转 3 步: [5,6,7,1,2,3,4]

class Solution:
    def moveIndex(self, nums, k):
        if len(nums) <2 or k ==0:
            return
        nums[::] = nums[::-1]
        nums[:k] = nums[:k][::-1]
        nums[k:] = nums[k:][::-1]
        print (nums)

if __name__=="__main__":
    nums = [1,2,3,4,5,6,7]
    k = 5
    s=Solution()
    s.moveIndex(nums,k)