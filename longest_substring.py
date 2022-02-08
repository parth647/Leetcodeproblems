class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if(s== " "):
            return 1
        hashmap = {}
        maxc = 0
        start = 0
        for i,c in enumerate(s):
            if(c in hashmap and start<=hashmap[c]):
                start = hashmap[c]+1
            else:
                maxc = max(maxc,i-start+1)
            
            hashmap[c] = i
        return maxc