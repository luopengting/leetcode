#
# @lc app=leetcode.cn id=547 lang=python
#
# [547] 朋友圈
#

# @lc code=start
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        len_M = len(M)
        cnt = len_M
        circle = [[i] for i in range(len_M)]
        for i in range(len_M):
            for j in range(i):
                if M[i][j] == 0:
                    continue
                
                if circle[i] is not circle[j]:
                    circle[i] += circle[j]
                    for firend in circle[j]:
                        circle[firend] = circle[i]
                    cnt -= 1

        return cnt

# @lc code=end

"""

if __name__ == "__main__":
    solution = Solution()

    M = [[1,1,0],[1,1,0],[0,0,1]]
    res = solution.findCircleNum(M)
    assert 2 == res

    M = [[1,1,0], [1,1,1], [0,1,1]]
    res = solution.findCircleNum(M)
    assert 1 == res

    M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]
    res = solution.findCircleNum(M)
    assert 1 == res

    M = [[1,1,1],[1,1,1],[1,1,1]]
    res = solution.findCircleNum(M)
    assert 1 == res
"""
