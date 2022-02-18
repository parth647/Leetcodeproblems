class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        hashmap = {0:1,1:0}
        for i in range(len(image)):
            row = image[i]
            left = 0
            right = len(row)-1
            while(left<right):
                temp = image[i][left]
                image[i][left] = image[i][right]
                image[i][right] = temp 
                image[i][left] = hashmap[image[i][left]]
                image[i][right] = hashmap[image[i][right]]
                # print(image[i],left,right)
                
                left+=1
                right-=1
            if(left==right):
                    image[i][left] = hashmap[image[i][left]]
        return image
        