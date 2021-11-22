# 题目描述
#
# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。
# 示例 1:
# 输入: "()"
# 输出: true
# 示例 2:
#
# 输入: "()[]{}"
# 输出: true
# 示例 3:
#
# 输入: "(]"
# 输出: false
# 示例 4:
#
# 输入: "([)]"
# 输出: false
# 示例 5:
#
# 输入: "{[]}"
# 输出: true
# 思路
#
# 关于这道题的思路，邓俊辉讲的非常好，没有看过的同学可以看一下，视频地址。
# 使用栈，遍历输入字符串;如果当前字符为左半边括号时，则将其压入栈中
# 如果遇到右半边括号时，分类讨论：
# 1）如栈不为空且为对应的左半边括号，则取出栈顶元素，继续循环
# 2）若此时栈为空，则直接返回 false
# 3）若不为对应的左半边括号，反之返回 false


class Solution:
    def validPath(self, s):
        stack = []
        map = {
            "{":"}",
            "[":"]",
            "(":")"
        }
        for s1 in s:
            print (s1)
            if s1 in map:
                stack.append(map[s1])
                print(stack)
            else:
                if len(stack) != 0:
                    top_element = stack.pop()
                    if s1 != top_element:
                        return False
                    else:
                        continue
                else:
                    return False
        print("validPath result:", stack, len(stack) == 0)
        return len(stack) == 0

    # 正则匹配,思路
    #
    # 我们不断通过消除
    # '[]' ， '()', '{}' ，最后判断剩下的是否是空串即可，就像开心消消乐一样。
    def validPath2(self, s):
        while "()" in s or "{}" in s or "()" in s:
            s.replace("()","").replace("[]", "").replace("{}","")
        print("validPath2 is:", s, not len(s))
        return len(s)


if __name__=="__main__":
    string1 = "([]}"
    fs=Solution()
    print(fs.validPath(string1))
    fs.validPath2(string1)