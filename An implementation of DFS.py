#An implementation of DFS
# Trial 1

class Solution:
    ans = []
    temp = []
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        def DFS(source):
            self.temp.append(source)
            if(source==n-1):#if the current node is target add it to the list and append li
                # self.temp.append(source)
                self.ans.append(self.temp)
                self.temp = [0]
                return
            for node in graph[source]:
                    # self.temp.append(node)
                DFS(node)
        DFS(0)
        return(self.ans)
        
        
    
       
        # base case
        
        