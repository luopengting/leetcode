#
# @lc app=leetcode.cn id=739 lang=python
#
# [739] 每日温度
#

# @lc code=start
class Solution(object):
    def dailyTemperatures(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        days = [0] * len(T)
        stack = []
        for index, temp in enumerate(T):
            while stack:
                top_index, top_temp = stack.pop(-1)
                if temp > top_temp:
                    days[top_index] = index - top_index
                else:
                    stack.append((top_index, top_temp))
                    stack.append((index, temp))
                    break
            stack.append((index, temp))
        return days

      
# @lc code=end

"""
if __name__ == "__main__":
    solution = Solution()

    T = [73,74,75,71,69,72,76,73]
    days = solution.dailyTemperatures(T)
    assert [1, 1, 4, 2, 1, 1, 0, 0] == days

    T = [89,62,70,58,47,47,46,76,100,70]
    days = solution.dailyTemperatures(T)
    print(days)
"""