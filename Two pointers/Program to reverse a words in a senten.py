# Program to reverse a words in a sentence

class Solution:
    def reverseWords(self, s: str) -> str:
        #strings are immutable in python
        temp = s.split(" ")
        result = ""
        for word in temp:
            word = word[::-1]
            result += word + " "
        return result[:-1]