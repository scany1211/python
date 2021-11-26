# 给你一个有序数组nums ，请你原地删除重复出现的元素，使每个元素只出现一次 ，返回删除后数组的新长度。#
# 不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。
# 说明:
# 为什么返回数值是整数，但输出的答案是数组呢?
# 请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。
# 你可以想象内部操作如下:
#
# // nums
# 是以“引用”方式传递的。也就是说，不对实参做任何拷贝
# int
# len = removeDuplicates(nums);
#
# // 在函数里修改输入数组对于调用者是可见的。
# // 根据你的函数返回的长度, 它会打印出数组中
# 该长度范围内
# 的所有元素。
# for (int i = 0; i < len; i++) {
#     print(nums[i]);
# }


class Solution:
    def duplicate(self, nums):
        """

        :type nums: object
        """
        cnt = 0 #记录重复的元素个数
        for i in range(1, len(nums)): # 1, 2, 3
            if nums[i-1] == nums[i]:
                cnt += 1
            else:
                nums[i - cnt] = nums[i]
            print(nums, i, cnt)
        return len(nums)-cnt
            # new_nums = set(nums)
        # print(list(new_nums))

    # 题目2：
    # 给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 最多出现两次 ，返回删除后数组的新长度。
    #
    # 不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。、
    # 解法
    #
    # 从数组下标1开始遍历数组。用计数器cnt记录当前数字重复出现的次数，cnt的最小计数为0；用cur 记录新数组下个待覆盖的元素位置。遍历时，若当前元素nums[i]
    # 与上个元素nums[i - 1]相同，则计数器 + 1，否则计数器重置为0。如果计数器小于2，说明当前元素nums[i]可以添加到新数组中，即：nums[cur] = nums[i]，同时
    # cur + +。遍历结果，返回cur值即可。
    def duplicate_2(self, nums):
        cnt, cur = 0, 1
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                cnt += 1
            else:
                cnt = 0
            if cnt < 2:
                nums[cur] = nums[i]
                cur += 1
            print(cnt, i, cur, nums)
        return cur
# 题目描述
# 找出数组中重复的数字。
# 在一个长度为 n 的数组 nums 里的所有数字都在 0 ～ n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。
# 示例 1：
# 输入：
# [2, 3, 1, 0, 2, 5, 3]
# 输出：2 或 3
# 解法
# 0 ～ n-1 范围内的数，分别还原到对应的位置上，如：数字 2 交换到下标为 2 的位置。
# 若交换过程中发现重复，则直接返回。
    def duplicate_3(self,nums2):
        for i, num in enumerate(nums2):
            while i != num:
                if num == nums2[num]:
                    print("find it:", num)
                    return num
                nums2[i], nums2[num] = nums2[num], nums2[i]
                num = nums2[i]
                print(nums2)
        return -1




if __name__ == "__main__":
    nums = [0,0,1,1,2,2,3,3,4,1]
    nums2 = [2, 3, 1, 0, 2, 5, 3]
    s = Solution()
    # s.duplicate(nums)
    # s.duplicate_2(nums)
    s.duplicate_3(nums2)