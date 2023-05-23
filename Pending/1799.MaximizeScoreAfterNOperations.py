from typing import List
import math

'''
elegir dos numeros maximo comun divisor * i devolver
'''
class Solution:
    def maxScore(self, nums: List[int]) -> int:
        n = len(nums) / 2
        math.gcd(1,2)
        for x in range(1, n + 1):
            pass

        return 0

if __name__ == "__main__":
    nums = [3, 4, 6, 8]
    sol = Solution().maxScore(nums)
    print(sol)

'''
You are given nums, an array of positive integers of size 2 * n. You must perform n operations on this array.

In the ith operation (1-indexed), you will:

Choose two elements, x and y.
Receive a score of i * gcd(x, y).
Remove x and y from nums.
Return the maximum score you can receive after performing n operations.

The function gcd(x, y) is the greatest common divisor of x and y.
'''