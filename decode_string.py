
# 394. Decode String
class Solution:
    def decodeString(self, s: str) -> str:
        s1 = []
        s2 = []
        main_s = ""
        temp_s =""
        for i in s:
            s1.append(i)
        while(s1):
            temp_c = s1.pop()
            if(temp_c=="["):
                s2.pop()
                temp_c = int(s1.pop())
                temp_s = temp_s*temp_c
                main_s+=temp_s
            elif(temp_c=="]"):
                temp_s = ""
                s2.append(temp_c)
            else:
                temp_s += temp_c
        return main_s[::-1]
            