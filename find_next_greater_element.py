# from xml.dom.minidom import Element


# Finding next greater Element

# The next greater element of some element x in an array is the first greater element that is to the right of x in the same array.

# You are given two distinct 0-indexed integer arrays nums1 and nums2, where nums1 is a subset of nums2.

# For each 0 <= i < nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1.

# Return an array ans of length nums1.length such that ans[i] is the next greater element as described above.


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        for it in nums2:
            while(stack and it>stack[-1]):
                item = stack.pop()
                hashmap[item] = it    
            stack.append(it)             
        ans = [0]*len(nums1)
        for i in range(len(nums1)):
            if(nums1[i] in hashmap):
                ans[i] = hashmap[nums1[i]]
            else:
                ans[i] = -1
        return ans
                
            
        