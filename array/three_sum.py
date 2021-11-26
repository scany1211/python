# 题目描述
#
# 给你一个包含n个整数的数组nums，判断nums中是否存在三个元素a，b，c ，使得a + b + c = 0 ？请你找出所有和为0且不重复的三元组。
#
# 注意：答案中不可以包含重复的三元组。
#
# 示例1：
#
# 输入：nums = [-1, 0, 1, 2, -1, -4]
# 输出：[[-1, -1, 2], [-1, 0, 1]]
#
# 思路1：
# 采用分治的思想找出三个数相加等于 0，我们可以数组依次遍历，每一项 a[i]我们都认为它是最终能够用组成 0 中的一个数字，那么我们的目标就是找到剩下的元素（除 a[i]）两个相加等于-a[i].
# 通过上面的思路，我们的问题转化为了给定一个数组，找出其中两个相加等于给定值，我们成功将问题转换为了另外一道力扣的简单题目1. 两数之和。这个问题是比较简单的， 我们只需要对数组进行排序，然后双指针解决即可。 加上需要外层遍历依次数组，因此总的时间复杂度应该是 O(N^2)。
#
# 思路2:
# “排序 + 双指针”实现。
class Solution:
    def threeSum(self, nums, target):
        res, n = [], len(nums)
        if n <3:
            return res
        nums.sort()
        print (nums)
        for i in range(n-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i +1
            k = n-1
            while j < k:
                print(nums[i], nums[j], nums[k], res)
                if nums[i] + nums[j] + nums[k] == target:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while j < n and nums[j] == nums[j-1]:
                        j += 1
                    while k > j and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[i] + nums[j] + nums[k] < target:
                    j += 1
                else:
                    k -= 1
                # print(nums[i], nums[j], nums[k], res)
        return res
    # def threeSum2(self, nums, target):
    #     res, n, helper = [], len(nums), {}
    #     if n <3:
    #         return res
    #     nums.sort()
    #     print(nums)
    #     for i in range(n-2):
    #         j = i+1
    #         for index, v in enumerate(nums[j:]):
    #             diff = target - nums[i] - v
    #             if diff in helper:
    #                 res.append([i, index+1+i, helper[diff]])
    #             helper[v] = index+1+i
    #             print(nums[i], v, diff, helper, res)
    #     return res, set(res)


    def fourSum(self, nums, target):
        n, res = len(nums), []
        nums.sort()
        for i in range(n-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if j > 0 and nums[j] == nums[j-1]:
                    continue
                k, l = j+1, n-1
                while k < l:
                    if nums[i] + nums[j] + nums[k] + nums[l] == target:
                        res.append([nums[i], nums[j],  nums[k], nums[l]])
                        k += 1
                        l -= 1
                        while k < n-2 and nums[k] == nums[k-1]:
                            k += 1
                        while l > k and nums[l] == nums[l+1]:
                            l -= 1
                    elif nums[i] + nums[j] + nums[k] + nums[l] < target:
                        k += 1
                    else:
                        l -= 1
        return res

    def testContinue(self, nums):
        for i in range(0, len(nums)-1):
            if nums[i] > 0:
                continue
            else:
                print (nums[i])

    # 给定一个长度为n的整数数组和一个目标值target，寻找能够使条件nums[i] + nums[j] + nums[k] < target成立的三元组i, j, k个数（0 <= i < j < k < n）。
    # 示例：
    # 输入: nums = [-2, 0, 1, 3], target = 2
    # 输出: 2
    # 解释: 因为一共有两个三元组满足累加和小于
    # 2:
    # [-2, 0, 1]
    # [-2, 0, 3]
    # 第二种思路：
    # 看到 i < j < k， 可以联想到先把nums排好序，
    # 然后利用一重外循环，一重内部双指针处理有序数组的两数之和问题。

    def minThreeSum(self, nums, target):
        cnt, l = 0, len(nums)
        nums.sort()
        print (nums)
        for i in range(l-2):
            midNum = target - nums[i]
            left = i + 1
            right = l - 1
            if nums[left] + nums[right] < midNum:
                cnt += right - left
                left += 1
                print(nums[i], nums[left], nums[right])
            else:
                right -= 1
        return cnt

    # 给定一个包括n个整数的数组nums和一个目标值target。找出nums中的三个整数，使得它们的和与target最接近。返回这三个数的和。假定每组输入只存在唯一答案。
    #
    # 例如，给定数组
    # nums = [-1，2，1，-4], 和
    # target = 1.
    #
    # 与
    # target
    # 最接近的三个数的和为
    # 2.(-1 + 2 + 1 = 2).

    def closeThreeSum(self, nums, target):
        cnt, l = 0, len(nums)
        nums.sort()
        cns = nums[o]+nums[1]+nums[2]
        for i in range(l-2):
            left = i + 1
            right = l - 1
            tmp = nums[i] + nums[left] + nums[right]
            while left < right:
                if abs(tmp - target) < abs(cns-target):
                    cns = tmp
                if tmp > target:
                    right -= 1
                else:
                    left += 1
        return cns

if __name__=="__main__":
    nums = [1,0,-1,0,-2,2]
    nums2 = [-2,0,1,3]
    target = 2
    s = Solution()
    # s.testContinue(nums)
    # print(s.threeSum(nums, target))
    # print(s.fourSum(nums, target))
    print(s.minThreeSum(nums2, target))