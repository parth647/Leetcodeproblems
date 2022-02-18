# # Interval List Intersections
# You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

# Return the intersection of these two interval lists.

# A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

# The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        i = 0
        j = 0
        ans = []
        while(i<len(firstList) and j<len(secondList)):
            a = firstList[i]
            b = secondList[j]
            if(a[1]<b[0]):
                i+=1
            elif(b[1]<a[0]):
                j+=1
            else:
                if(a[1]<b[1]):
                    i+=1
                else:
                    j+=1
                ans.append([max(a[0],b[0]),min(a[1],b[1])])
        return ans
        
            
        
        