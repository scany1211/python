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

if __name__=="__main__":
    nums = [1,0,-1,0,-2,2]
    target = 0
    s = Solution()
    # s.testContinue(nums)
    # print(s.threeSum(nums, target))
    print(s.fourSum(nums, target))