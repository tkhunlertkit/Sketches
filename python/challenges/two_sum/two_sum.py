import itertools

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        for (val1, val2) in itertools.combinations(nums, 2):
            if val1 + val2 == target:
                i = nums.index(val1)
                j = nums.index(val2, i + 1)
                return [i, j]

if __name__ == '__main__':
    nums = [0,4,3,0]
    target = 0
    print (Solution().twoSum(nums, target))