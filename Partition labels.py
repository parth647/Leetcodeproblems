# Partition labels


# You are given a string s. We want to partition the string into as many parts as possible so that each letter appears in at most one part.

# Note that the partition is done so that after concatenating all the parts in order, the resultant string should be s.

# Return a list of integers representing the size of these parts.

#slow solution
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        hashmap = {}
        ans = []
        for i in range(len(s)):
            if(s[i] in hashmap):
                hashmap[s[i]][1] = i
            else:
                hashmap[s[i]] = [i,i]
        
        mini,maxi = hashmap[s[0]][0],hashmap[s[0]][1]
        group=1
        # print(hashmap)
        for i in range(1,len(s)):
            # print(maxi)
            if(hashmap[s[i]][0]>maxi):
                ans.append(group)
                group = 1
                
            else:
                group+=1
            maxi = max(maxi,hashmap[s[i]][1])
                
            
        ans.append(group)    
        return(ans)
                
#Better solution
        
                