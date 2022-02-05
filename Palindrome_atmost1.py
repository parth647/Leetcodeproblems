class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        left = 0
        right = len(s)-1
        flag = 0
        while(left<right):
            if(s[left]!=s[right]):
                first,second = s[left:right],s[left+1:right+1]
                return(first==first[::-1] or second==second[::-1])
            left+=1
            right-=1
        return True
              

# Time Complexity O(n)
#  Space Complexity O(n)