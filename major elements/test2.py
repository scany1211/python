from typing import List
#
# 题目描述
#
# 给定一个大小为
# n
# 的数组，找到其中的多数元素。多数元素是指在数组中出现次数
# 大于 ⌊ n / 2 ⌋ 的元素。
#
# 你可以假设数组是非空的，并且给定的数组总是存在多数元素。
#
#
#
# 示例
# 1：
#
# 输入：[3, 2, 3]
# 输出：3
#
# 示例
# 2：
#
# 输入：[2, 2, 1, 1, 1, 2, 2]
# 输出：2
#1. 解题思路：通过消除不同元素直到没有不同元素
# 摩尔投票算法就是把相异的2个数都消耗掉，由于总是存在多数元素，意味着相异的数消耗掉之后只可能留下那个多数元素。具体过程如下，用result记录最终的那个多数，初始化为数组的第一个元素，count记录这个数字重复的次数：
#
#     首先，如果count为0，表示前面的相异的数字都消耗完了，result赋值为当前的数，count为1；
#
#     如果count大于0：
#         如果result和当前元素相等，则count加1；
#         如果result和当前元素不相等，则count减一，即消耗掉一对相异的数。

class Solution:
    def major_el(self, nums):
        cnt = major = 0
        for num in nums:
            if cnt == 0:
                major = num
                cnt = 1
            else:
                cnt += (1 if major == num else -1)
            print(major, num, cnt)
        return major

if __name__ == "__main__":
    # nums = [2,1,2,3,4,5,2,2,2]
    testnum = [2, 1, 3, 4, 5]
    s = Solution()
    print(s.major_el(testnum))
