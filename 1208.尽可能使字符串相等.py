#
# @lc app=leetcode.cn id=1208 lang=python
#
# [1208] 尽可能使字符串相等
#

# @lc code=start
class Solution(object):
    def equalSubstring(self, s, t, maxCost):
        """
        :type s: str
        :type t: str
        :type maxCost: int
        :rtype: int
        """
        left, right = 0, 0
        length = len(s)
        while right < length:
            if abs(ord(s[right]) - ord(t[right])) <= maxCost:
               maxCost -= abs(ord(s[right]) - ord(t[right]))
               right += 1
            else:
                maxCost += abs(ord(s[left]) - ord(t[left]))
                maxCost -= abs(ord(s[right]) - ord(t[right]))
                left += 1
                right += 1

        return right - left

# @lc code=end
"""
if __name__ == "__main__":
    solution = Solution()

    s = "abcd"
    t = "bcdf"
    cost = 3
    res = solution.equalSubstring(s, t, cost)
    assert 3 == res

    s = "abcd"
    t = "bcdf"
    cost = 1
    res = solution.equalSubstring(s, t, cost)
    assert 1 == res

    s = "a"
    t = "b"
    cost = 1
    res = solution.equalSubstring(s, t, cost)
    assert 1 == res
"""