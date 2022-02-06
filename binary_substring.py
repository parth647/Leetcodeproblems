class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        #count number of consec 0's and 1's
        prev = s[0]
        freq = []
        i = 1
        temp_count = 1
        while(i<len(s)):
            if(s[i]==prev):
                temp_count+=1
            else:
                freq.append(temp_count)
                prev = s[i]
                temp_count = 1
            i+=1
        freq.append(temp_count)
        ans = 0
        for index in range(1,len(freq)):
            ans+=min(freq[index],freq[index-1])
        return ans
            
            
        