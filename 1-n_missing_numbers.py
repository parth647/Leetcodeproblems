
# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.
# Time : O(N)
# Space : O(N)
# Think of doing this in constant space

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ans = []
        set_nums = set(nums)
        for i in range(1,len(nums)+1):
            if i not in set_nums:
                ans.append(i)
        return ans
        