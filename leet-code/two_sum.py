# 两数之和

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for index, num in enumerate(nums):
            result = target - num
            if result in hash_map:
                return [hash_map[result], index]
            hash_map[num] = index

        return []