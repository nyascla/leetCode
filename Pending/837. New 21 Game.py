'''

'''
class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        pass

if __name__ == "__main__":
    nums1 = [1,4,2]
    nums2 = [1,2,4]
    sol = Solution().maxUncrossedLines(nums1, nums2)

'''
Alice plays the following game, loosely based on the card game "21".

Alice starts with 0 points and draws numbers while she has less than k points. During each draw, she gains an integer number of points randomly from the range [1, maxPts], where maxPts is an integer. Each draw is independent and the outcomes have equal probabilities.

Alice stops drawing numbers when she gets k or more points.

Return the probability that Alice has n or fewer points.

Answers within 10-5 of the actual answer are considered accepted.
'''