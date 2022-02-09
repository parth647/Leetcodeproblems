class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = abs(arr[1]-arr[0])
        ans = []
        # ans = [[arr[0],arr[1]]]
        
        for i in range(len(arr)-1):
            curr_diff = abs(arr[i+1]-arr[i])
            if(curr_diff == diff):
                ans.append([arr[i],arr[i+1]])
            elif(curr_diff < diff):
                ans = [[arr[i],arr[i+1]]]
                diff = curr_diff
                
                
                
        return ans
        