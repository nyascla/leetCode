'''
matriz, cuantos caminos hay para llegar de la esquina superior izquierda a la inferior derecha
'''
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        def dfs(x, y):
            if x == 0 and y == 0:
                return 1
            if (x, y) in dp:
                return dp[(x, y)]

            paths = 0
            # up
            if x - 1 >= 0:
                paths += dfs(x - 1, y)

            # right
            if y - 1 >= 0:
                paths += dfs(x, y - 1)

            dp[(x, y)] = paths
            return paths

        dp = {}
        return dfs(m - 1, n - 1)

if __name__ == "__main__":
    m, n = 3, 2
    sol = Solution().uniquePaths(m, n)
    print(sol)
'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The test cases are generated so that the answer will be less than or equal to 2 * 109.
Math
Dynamic Programming
Combinatorics
'''