class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.arr = wordsDict
        self.hashmap = {}
        for i in range(len(self.arr)):
            if self.arr[i] in self.hashmap:
                self.hashmap[self.arr[i]].append(i)
            else:
                self.hashmap[self.arr[i]] = [i]
        

    def shortest(self, word1: str, word2: str) -> int:
        # print(self.hashmap)
        # print(word1,max(self.hashmap[word1]))
        l1,l2 = 0,0
        loc1 = self.hashmap[word1]
        loc2 = self.hashmap[word2]
        min_diff = float("inf")
        while(l1<len(loc1) and l2<len(loc2)):
            min_diff = min(min_diff,abs(loc1[l1]-loc2[l2]))
            if(loc1[l1]>loc2[l2]):
                l2+=1
            else:
                l1+=1
        return min_diff
        
    
        


# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)